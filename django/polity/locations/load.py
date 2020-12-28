from pathlib import Path
from django.contrib.gis.utils import LayerMapping

from locations.models import Country, Region, Canton, Municipality, PLZ


"""
* load initial .shp data from swisstopo
    https://docs.djangoproject.com/en/3.1/ref/contrib/gis/tutorial/
* see locations.models for more details
* how to import:
    ./manage.py shell
    from locations import load
    load.canton_import() (e.g.)
* order of importing:
    1. country
    2. canton
    3. regions (fk canton depends on canton)
    4. municipality (fk canton + fk region)
"""

# rewriting layermapping for municipality_import() -> line 56

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.gis.db.models import GeometryField
from django.db import models
class LayerMapError(Exception):
    pass

class MissingForeignKey(LayerMapError):
    pass
class CustomLayerMapping(LayerMapping):
    def feature_kwargs(self, feat):
        """
        Given an OGR Feature, return a dictionary of keyword arguments for
        constructing the mapped model.
        """
        # The keyword arguments for model construction.
        kwargs = {}

        # Incrementing through each model field and OGR field in the
        # dictionary mapping.
        for field_name, ogr_name in self.mapping.items():
            model_field = self.fields[field_name]

            if isinstance(model_field, GeometryField):
                # Verify OGR geometry.
                try:
                    val = self.verify_geom(feat.geom, model_field)
                except GDALException:
                    raise LayerMapError('Could not retrieve geometry from feature.')
            elif isinstance(model_field, models.base.ModelBase):
                # The related _model_, not a field was passed in -- indicating
                # another mapping for the related Model.
                try: 
                    # original code
                    val = self.verify_fk(feat, model_field, ogr_name)
                except MissingForeignKey:
                    # if foreignkey not found in model_field -> just leave the field empty (need null/blank=true in model)
                    val = None
            else:
                # Otherwise, verify OGR Field type.
                val = self.verify_ogr_field(feat[ogr_name], model_field)

            # Setting the keyword arguments for the field name with the
            # value obtained above.
            kwargs[field_name] = val

        return kwargs
    
    def verify_fk(self, feat, rel_model, rel_mapping):
        """
        Given an OGR Feature, the related model and its dictionary mapping,
        retrieve the related model for the ForeignKey mapping.
        """
        # TODO: It is expensive to retrieve a model for every record --
        #  explore if an efficient mechanism exists for caching related
        #  ForeignKey models.

        # Constructing and verifying the related model keyword arguments.
        fk_kwargs = {}
        for field_name, ogr_name in rel_mapping.items():
            fk_kwargs[field_name] = self.verify_ogr_field(feat[ogr_name], rel_model._meta.get_field(field_name))

        # Attempting to retrieve and return the related model.
        try:
            return rel_model.objects.using(self.using).get(**fk_kwargs)
        except ObjectDoesNotExist:
            raise MissingForeignKey(
                'No ForeignKey %s model found with keyword arguments: %s' %
                (rel_model.__name__, fk_kwargs)
            )

# mapping + import country

country_shp = 'locations/data/swissBOUNDARIES/swissBOUNDARIES3D_1_3_TLM_LANDESGEBIET.shp'
country_mapping = {
    'uuid': 'UUID',
    'objektart': 'OBJEKTART',
    'revision_q': 'REVISION_Q',
    'icc': 'ICC',
    'see_flaech': 'SEE_FLAECH',
    'name': 'NAME',
    'einwohnerz': 'EINWOHNERZ',
    'landesflae': 'LANDESFLAE',
    'land_teil': 'LAND_TEIL',
    'geom': 'MULTIPOLYGON25D',
}
def country_import(verbose=True):
    lm = LayerMapping(Country, str(country_shp), country_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)

# mapping + import region

region_shp = 'locations/data/swissBOUNDARIES/swissBOUNDARIES3D_1_3_TLM_BEZIRKSGEBIET.shp'
region_mapping = {
    'uuid': 'UUID',
    'objektart': 'OBJEKTART',
    'bezirksnum': 'BEZIRKSNUM',
    'see_flaech': 'SEE_FLAECH',
    'revision_q': 'REVISION_Q',
    'bezirksfla': 'BEZIRKSFLA',
    'bezirk_tei': 'BEZIRK_TEI',
    'name': 'NAME',
    'kantonsnum': { 'kantonsnum': 'KANTONSNUM' },
    'icc': 'ICC',
    'einwohnerz': 'EINWOHNERZ',
    'geom': 'MULTIPOLYGON25D',
}
def region_import(verbose=True):
    lm = LayerMapping(Region, str(region_shp), region_mapping, transform=True, unique=('name', 'bezirksnum',))
    lm.save(strict=True, verbose=verbose)

# mapping + import canton

canton_shp = 'locations/data/swissBOUNDARIES/swissBOUNDARIES3D_1_3_TLM_KANTONSGEBIET.shp'
canton_map = {
    'uuid': 'UUID',
    'kantonsnum': 'KANTONSNUM',
    'objektart': 'OBJEKTART',
    'revision_q': 'REVISION_Q',
    'icc': 'ICC',
    'see_flaech': 'SEE_FLAECH',
    'kantonsfla': 'KANTONSFLA',
    'kt_teil': 'KT_TEIL',
    'name': 'NAME',
    'einwohnerz': 'EINWOHNERZ',
    'geom': 'MULTIPOLYGON25D',
}
def canton_import(verbose=True):
    # unique = updates existing entries and adds geom to that (no duplicates)
    lm = LayerMapping(Canton, str(canton_shp), canton_map, transform=True, unique=('name', 'kantonsnum',))
    lm.save(strict=True, verbose=verbose)

# mapping + import municipality (with CustomLayerMapping)

municipality_shp = 'locations/data/swissBOUNDARIES/swissBOUNDARIES3D_1_3_TLM_HOHEITSGEBIET.shp'
municipality_mapping = {
    'uuid': 'UUID',
    'objektart': 'OBJEKTART',
    'bezirksnum': { 'bezirksnum': 'BEZIRKSNUM' }, # foreign key need to be dictionary
    'see_flaech': 'SEE_FLAECH',
    'revision_q': 'REVISION_Q',
    'name': 'NAME',
    'kantonsnum': { 'kantonsnum': 'KANTONSNUM' }, 
    'icc': 'ICC',
    'einwohnerz': 'EINWOHNERZ',
    'bfs_nummer': 'BFS_NUMMER',
    'gem_teil': 'GEM_TEIL',
    'gem_flaech': 'GEM_FLAECH',
    'shn': 'SHN',
    'geom': 'MULTIPOLYGON25D',
}
def municipality_import(verbose=True):
    lm = CustomLayerMapping(Municipality, str(municipality_shp), municipality_mapping, transform=True, unique=('name', 'bfs_nummer',))
    # not strict because of foreign municipalities (DE, IT, Liechtenstein) -> error when trying to connect foreign key
    lm.save(strict=True, verbose=verbose)
