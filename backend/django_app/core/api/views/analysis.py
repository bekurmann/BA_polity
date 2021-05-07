from rest_framework.views import APIView
from rest_framework.response import Response

from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Affair, Membership


class AnalysisParlamentAffairsPerYearOW(APIView):
    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # all affairs
    affair_count_2010 = Affair.objects.filter(parlament=100, date_received__year=2010).count()
    affair_count_2011 = Affair.objects.filter(parlament=100, date_received__year=2011).count()
    affair_count_2012 = Affair.objects.filter(parlament=100, date_received__year=2012).count()
    affair_count_2013 = Affair.objects.filter(parlament=100, date_received__year=2013).count()
    affair_count_2014 = Affair.objects.filter(parlament=100, date_received__year=2014).count()
    affair_count_2015 = Affair.objects.filter(parlament=100, date_received__year=2015).count()
    affair_count_2016 = Affair.objects.filter(parlament=100, date_received__year=2016).count()
    affair_count_2017 = Affair.objects.filter(parlament=100, date_received__year=2017).count()
    affair_count_2018 = Affair.objects.filter(parlament=100, date_received__year=2018).count()
    affair_count_2019 = Affair.objects.filter(parlament=100, date_received__year=2019).count()
    affair_count_2020 = Affair.objects.filter(parlament=100, date_received__year=2020).count()

    # affairs sp
    affair_count_2010_sp = Affair.objects.filter(parlament=100, date_received__year=2010, signatory__fractions=1).count()
    affair_count_2011_sp = Affair.objects.filter(parlament=100, date_received__year=2011, signatory__fractions=1).count()
    affair_count_2012_sp = Affair.objects.filter(parlament=100, date_received__year=2012, signatory__fractions=1).count()
    affair_count_2013_sp = Affair.objects.filter(parlament=100, date_received__year=2013, signatory__fractions=1).count()
    affair_count_2014_sp = Affair.objects.filter(parlament=100, date_received__year=2014, signatory__fractions=1).count()
    affair_count_2015_sp = Affair.objects.filter(parlament=100, date_received__year=2015, signatory__fractions=1).count()
    affair_count_2016_sp = Affair.objects.filter(parlament=100, date_received__year=2016, signatory__fractions=1).count()
    affair_count_2017_sp = Affair.objects.filter(parlament=100, date_received__year=2017, signatory__fractions=1).count()
    affair_count_2018_sp = Affair.objects.filter(parlament=100, date_received__year=2018, signatory__fractions=1).count()
    affair_count_2019_sp = Affair.objects.filter(parlament=100, date_received__year=2019, signatory__fractions=1).count()
    affair_count_2020_sp = Affair.objects.filter(parlament=100, date_received__year=2020, signatory__fractions=1).count()

    # affairs cvp
    affair_count_2010_cvp = Affair.objects.filter(parlament=100, date_received__year=2010, signatory__fractions=5).count()
    affair_count_2011_cvp = Affair.objects.filter(parlament=100, date_received__year=2011, signatory__fractions=5).count()
    affair_count_2012_cvp = Affair.objects.filter(parlament=100, date_received__year=2012, signatory__fractions=5).count()
    affair_count_2013_cvp = Affair.objects.filter(parlament=100, date_received__year=2013, signatory__fractions=5).count()
    affair_count_2014_cvp = Affair.objects.filter(parlament=100, date_received__year=2014, signatory__fractions=5).count()
    affair_count_2015_cvp = Affair.objects.filter(parlament=100, date_received__year=2015, signatory__fractions=5).count()
    affair_count_2016_cvp = Affair.objects.filter(parlament=100, date_received__year=2016, signatory__fractions=5).count()
    affair_count_2017_cvp = Affair.objects.filter(parlament=100, date_received__year=2017, signatory__fractions=5).count()
    affair_count_2018_cvp = Affair.objects.filter(parlament=100, date_received__year=2018, signatory__fractions=5).count()
    affair_count_2019_cvp = Affair.objects.filter(parlament=100, date_received__year=2019, signatory__fractions=5).count()
    affair_count_2020_cvp = Affair.objects.filter(parlament=100, date_received__year=2020, signatory__fractions=5).count()

    # affairs fdp
    affair_count_2010_fdp = Affair.objects.filter(parlament=100, date_received__year=2010, signatory__fractions=4).count()
    affair_count_2011_fdp = Affair.objects.filter(parlament=100, date_received__year=2011, signatory__fractions=4).count()
    affair_count_2012_fdp = Affair.objects.filter(parlament=100, date_received__year=2012, signatory__fractions=4).count()
    affair_count_2013_fdp = Affair.objects.filter(parlament=100, date_received__year=2013, signatory__fractions=4).count()
    affair_count_2014_fdp = Affair.objects.filter(parlament=100, date_received__year=2014, signatory__fractions=4).count()
    affair_count_2015_fdp = Affair.objects.filter(parlament=100, date_received__year=2015, signatory__fractions=4).count()
    affair_count_2016_fdp = Affair.objects.filter(parlament=100, date_received__year=2016, signatory__fractions=4).count()
    affair_count_2017_fdp = Affair.objects.filter(parlament=100, date_received__year=2017, signatory__fractions=4).count()
    affair_count_2018_fdp = Affair.objects.filter(parlament=100, date_received__year=2018, signatory__fractions=4).count()
    affair_count_2019_fdp = Affair.objects.filter(parlament=100, date_received__year=2019, signatory__fractions=4).count()
    affair_count_2020_fdp = Affair.objects.filter(parlament=100, date_received__year=2020, signatory__fractions=4).count()

    # affairs svp
    affair_count_2010_svp = Affair.objects.filter(parlament=100, date_received__year=2010, signatory__fractions=3).count()
    affair_count_2011_svp = Affair.objects.filter(parlament=100, date_received__year=2011, signatory__fractions=3).count()
    affair_count_2012_svp = Affair.objects.filter(parlament=100, date_received__year=2012, signatory__fractions=3).count()
    affair_count_2013_svp = Affair.objects.filter(parlament=100, date_received__year=2013, signatory__fractions=3).count()
    affair_count_2014_svp = Affair.objects.filter(parlament=100, date_received__year=2014, signatory__fractions=3).count()
    affair_count_2015_svp = Affair.objects.filter(parlament=100, date_received__year=2015, signatory__fractions=3).count()
    affair_count_2016_svp = Affair.objects.filter(parlament=100, date_received__year=2016, signatory__fractions=3).count()
    affair_count_2017_svp = Affair.objects.filter(parlament=100, date_received__year=2017, signatory__fractions=3).count()
    affair_count_2018_svp = Affair.objects.filter(parlament=100, date_received__year=2018, signatory__fractions=3).count()
    affair_count_2019_svp = Affair.objects.filter(parlament=100, date_received__year=2019, signatory__fractions=3).count()
    affair_count_2020_svp = Affair.objects.filter(parlament=100, date_received__year=2020, signatory__fractions=3).count()

    # affairs csp
    affair_count_2010_csp = Affair.objects.filter(parlament=100, date_received__year=2010, signatory__fractions=2).count()
    affair_count_2011_csp = Affair.objects.filter(parlament=100, date_received__year=2011, signatory__fractions=2).count()
    affair_count_2012_csp = Affair.objects.filter(parlament=100, date_received__year=2012, signatory__fractions=2).count()
    affair_count_2013_csp = Affair.objects.filter(parlament=100, date_received__year=2013, signatory__fractions=2).count()
    affair_count_2014_csp = Affair.objects.filter(parlament=100, date_received__year=2014, signatory__fractions=2).count()
    affair_count_2015_csp = Affair.objects.filter(parlament=100, date_received__year=2015, signatory__fractions=2).count()
    affair_count_2016_csp = Affair.objects.filter(parlament=100, date_received__year=2016, signatory__fractions=2).count()
    affair_count_2017_csp = Affair.objects.filter(parlament=100, date_received__year=2017, signatory__fractions=2).count()
    affair_count_2018_csp = Affair.objects.filter(parlament=100, date_received__year=2018, signatory__fractions=2).count()
    affair_count_2019_csp = Affair.objects.filter(parlament=100, date_received__year=2019, signatory__fractions=2).count()
    affair_count_2020_csp = Affair.objects.filter(parlament=100, date_received__year=2020, signatory__fractions=2).count()

    def get(self, request, format=None):
        data = {
            "labels": ["2010", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",],
            "data_all": [
                self.affair_count_2010, self.affair_count_2011, self.affair_count_2012, self.affair_count_2013,
                self.affair_count_2014, self.affair_count_2015, self.affair_count_2016, self.affair_count_2017,
                self.affair_count_2018, self.affair_count_2019, self.affair_count_2020,
            ],
            "data_sp": [
                self.affair_count_2010_sp, self.affair_count_2011_sp, self.affair_count_2012_sp, self.affair_count_2013_sp, 
                self.affair_count_2014_sp, self.affair_count_2015_sp, self.affair_count_2016_sp, self.affair_count_2017_sp, 
                self.affair_count_2018_sp, self.affair_count_2019_sp, self.affair_count_2020_sp, 
            ],
            "data_cvp": [
                self.affair_count_2010_cvp, self.affair_count_2011_cvp, self.affair_count_2012_cvp, self.affair_count_2013_cvp, 
                self.affair_count_2014_cvp, self.affair_count_2015_cvp, self.affair_count_2016_cvp, self.affair_count_2017_cvp, 
                self.affair_count_2018_cvp, self.affair_count_2019_cvp, self.affair_count_2020_cvp, 
            ],
            "data_fdp": [
                self.affair_count_2010_fdp, self.affair_count_2011_fdp, self.affair_count_2012_fdp, self.affair_count_2013_fdp, 
                self.affair_count_2014_fdp, self.affair_count_2015_fdp, self.affair_count_2016_fdp, self.affair_count_2017_fdp, 
                self.affair_count_2018_fdp, self.affair_count_2019_fdp, self.affair_count_2020_fdp, 
            ],
            "data_svp": [
                self.affair_count_2010_svp, self.affair_count_2011_svp, self.affair_count_2012_svp, self.affair_count_2013_svp, 
                self.affair_count_2014_svp, self.affair_count_2015_svp, self.affair_count_2016_svp, self.affair_count_2017_svp, 
                self.affair_count_2018_svp, self.affair_count_2019_svp, self.affair_count_2020_svp, 
            ],
            "data_csp": [
                self.affair_count_2010_csp, self.affair_count_2011_csp, self.affair_count_2012_csp, self.affair_count_2013_csp, 
                self.affair_count_2014_csp, self.affair_count_2015_csp, self.affair_count_2016_csp, self.affair_count_2017_csp, 
                self.affair_count_2018_csp, self.affair_count_2019_csp, self.affair_count_2020_csp, 
            ]
        }

        return Response(data)

class AnalysisParlamentAffairsTypesOW(APIView):
    """
    * returns total count of different types of affairs
    * returns total count of successful affairs per type
    """

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # type count
    motions = Affair.objects.filter(parlament=100, affair_type="MOTIO").count()
    people_motions = Affair.objects.filter(parlament=100, affair_type="PMOTI").count()
    postulates = Affair.objects.filter(parlament=100, affair_type="POSTU").count()
    interpellations = Affair.objects.filter(parlament=100, affair_type="INTER").count()
    inquiries = Affair.objects.filter(parlament=100, affair_type="INQUI").count()

    # type count successful
    suc_motions = Affair.objects.filter(parlament=100, affair_type="MOTIO", accepted=True).count()
    suc_people_motions = Affair.objects.filter(parlament=100, affair_type="PMOTI", accepted=True).count()
    suc_postulates = Affair.objects.filter(parlament=100, affair_type="POSTU", accepted=True).count()
    suc_interpellations = Affair.objects.filter(parlament=100, affair_type="INTER", accepted=True).count()
    suc_inquiries = Affair.objects.filter(parlament=100, affair_type="INQUI", accepted=True).count()

    def get(self, request, format=None):
        data = {
            "labels": ["Motions", "People Motions", "Postulates", "Interpellations", "Inquiries"],
            "data_all": [
                self.motions, self.people_motions, self.postulates, self.interpellations, self.inquiries,
            ],
            "data_success": [
                self.suc_motions, self.suc_people_motions, self.suc_postulates, self.suc_interpellations, self.suc_inquiries,
            ],
        }

        return Response(data)

class AnalysisParlamentAffairTypesPerYearOW(APIView):

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # affairs types count 2010
    affair_types_2010_inqui = Affair.objects.filter(parlament=100, date_received__year=2010, affair_type="INQUI").count()
    affair_types_2010_inter = Affair.objects.filter(parlament=100, date_received__year=2010, affair_type="INTER").count()
    affair_types_2010_postu = Affair.objects.filter(parlament=100, date_received__year=2010, affair_type="POSTU").count()
    affair_types_2010_motio = Affair.objects.filter(parlament=100, date_received__year=2010, affair_type="MOTIO").count()
    affair_types_2010_pmoti = Affair.objects.filter(parlament=100, date_received__year=2010, affair_type="PMOTI").count()

    # affairs types count 2011
    affair_types_2011_inqui = Affair.objects.filter(parlament=100, date_received__year=2011, affair_type="INQUI").count()
    affair_types_2011_inter = Affair.objects.filter(parlament=100, date_received__year=2011, affair_type="INTER").count()
    affair_types_2011_postu = Affair.objects.filter(parlament=100, date_received__year=2011, affair_type="POSTU").count()
    affair_types_2011_motio = Affair.objects.filter(parlament=100, date_received__year=2011, affair_type="MOTIO").count()
    affair_types_2011_pmoti = Affair.objects.filter(parlament=100, date_received__year=2011, affair_type="PMOTI").count()

    # affairs types count 2012
    affair_types_2012_inqui = Affair.objects.filter(parlament=100, date_received__year=2012, affair_type="INQUI").count()
    affair_types_2012_inter = Affair.objects.filter(parlament=100, date_received__year=2012, affair_type="INTER").count()
    affair_types_2012_postu = Affair.objects.filter(parlament=100, date_received__year=2012, affair_type="POSTU").count()
    affair_types_2012_motio = Affair.objects.filter(parlament=100, date_received__year=2012, affair_type="MOTIO").count()
    affair_types_2012_pmoti = Affair.objects.filter(parlament=100, date_received__year=2012, affair_type="PMOTI").count()

    # affairs types count 2013
    affair_types_2013_inqui = Affair.objects.filter(parlament=100, date_received__year=2013, affair_type="INQUI").count()
    affair_types_2013_inter = Affair.objects.filter(parlament=100, date_received__year=2013, affair_type="INTER").count()
    affair_types_2013_postu = Affair.objects.filter(parlament=100, date_received__year=2013, affair_type="POSTU").count()
    affair_types_2013_motio = Affair.objects.filter(parlament=100, date_received__year=2013, affair_type="MOTIO").count()
    affair_types_2013_pmoti = Affair.objects.filter(parlament=100, date_received__year=2013, affair_type="PMOTI").count()

    # affairs types count 2014
    affair_types_2014_inqui = Affair.objects.filter(parlament=100, date_received__year=2014, affair_type="INQUI").count()
    affair_types_2014_inter = Affair.objects.filter(parlament=100, date_received__year=2014, affair_type="INTER").count()
    affair_types_2014_postu = Affair.objects.filter(parlament=100, date_received__year=2014, affair_type="POSTU").count()
    affair_types_2014_motio = Affair.objects.filter(parlament=100, date_received__year=2014, affair_type="MOTIO").count()
    affair_types_2014_pmoti = Affair.objects.filter(parlament=100, date_received__year=2014, affair_type="PMOTI").count()

    # affairs types count 2015
    affair_types_2015_inqui = Affair.objects.filter(parlament=100, date_received__year=2015, affair_type="INQUI").count()
    affair_types_2015_inter = Affair.objects.filter(parlament=100, date_received__year=2015, affair_type="INTER").count()
    affair_types_2015_postu = Affair.objects.filter(parlament=100, date_received__year=2015, affair_type="POSTU").count()
    affair_types_2015_motio = Affair.objects.filter(parlament=100, date_received__year=2015, affair_type="MOTIO").count()
    affair_types_2015_pmoti = Affair.objects.filter(parlament=100, date_received__year=2015, affair_type="PMOTI").count()

    # affairs types count 2016
    affair_types_2016_inqui = Affair.objects.filter(parlament=100, date_received__year=2016, affair_type="INQUI").count()
    affair_types_2016_inter = Affair.objects.filter(parlament=100, date_received__year=2016, affair_type="INTER").count()
    affair_types_2016_postu = Affair.objects.filter(parlament=100, date_received__year=2016, affair_type="POSTU").count()
    affair_types_2016_motio = Affair.objects.filter(parlament=100, date_received__year=2016, affair_type="MOTIO").count()
    affair_types_2016_pmoti = Affair.objects.filter(parlament=100, date_received__year=2016, affair_type="PMOTI").count()

    # affairs types count 2017
    affair_types_2017_inqui = Affair.objects.filter(parlament=100, date_received__year=2017, affair_type="INQUI").count()
    affair_types_2017_inter = Affair.objects.filter(parlament=100, date_received__year=2017, affair_type="INTER").count()
    affair_types_2017_postu = Affair.objects.filter(parlament=100, date_received__year=2017, affair_type="POSTU").count()
    affair_types_2017_motio = Affair.objects.filter(parlament=100, date_received__year=2017, affair_type="MOTIO").count()
    affair_types_2017_pmoti = Affair.objects.filter(parlament=100, date_received__year=2017, affair_type="PMOTI").count()

    # affairs types count 2018
    affair_types_2018_inqui = Affair.objects.filter(parlament=100, date_received__year=2018, affair_type="INQUI").count()
    affair_types_2018_inter = Affair.objects.filter(parlament=100, date_received__year=2018, affair_type="INTER").count()
    affair_types_2018_postu = Affair.objects.filter(parlament=100, date_received__year=2018, affair_type="POSTU").count()
    affair_types_2018_motio = Affair.objects.filter(parlament=100, date_received__year=2018, affair_type="MOTIO").count()
    affair_types_2018_pmoti = Affair.objects.filter(parlament=100, date_received__year=2018, affair_type="PMOTI").count()

    # affairs types count 2019
    affair_types_2019_inqui = Affair.objects.filter(parlament=100, date_received__year=2019, affair_type="INQUI").count()
    affair_types_2019_inter = Affair.objects.filter(parlament=100, date_received__year=2019, affair_type="INTER").count()
    affair_types_2019_postu = Affair.objects.filter(parlament=100, date_received__year=2019, affair_type="POSTU").count()
    affair_types_2019_motio = Affair.objects.filter(parlament=100, date_received__year=2019, affair_type="MOTIO").count()
    affair_types_2019_pmoti = Affair.objects.filter(parlament=100, date_received__year=2019, affair_type="PMOTI").count()

    # affairs types count 2020
    affair_types_2020_inqui = Affair.objects.filter(parlament=100, date_received__year=2020, affair_type="INQUI").count()
    affair_types_2020_inter = Affair.objects.filter(parlament=100, date_received__year=2020, affair_type="INTER").count()
    affair_types_2020_postu = Affair.objects.filter(parlament=100, date_received__year=2020, affair_type="POSTU").count()
    affair_types_2020_motio = Affair.objects.filter(parlament=100, date_received__year=2020, affair_type="MOTIO").count()
    affair_types_2020_pmoti = Affair.objects.filter(parlament=100, date_received__year=2020, affair_type="PMOTI").count()

    def get(self, request, format=None):
        data = {
            "labels_years": ["2010", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",],
            "data_inqui": [
                #inquiries per year
                self.affair_types_2010_inqui, self.affair_types_2011_inqui, self.affair_types_2012_inqui,
                self.affair_types_2013_inqui, self.affair_types_2014_inqui, self.affair_types_2015_inqui,
                self.affair_types_2016_inqui, self.affair_types_2017_inqui, self.affair_types_2018_inqui,
                self.affair_types_2019_inqui, self.affair_types_2020_inqui,
            ],
            "data_inter": [
                #interepellation per year
                self.affair_types_2010_inter,
                self.affair_types_2011_inter,
                self.affair_types_2012_inter,
                self.affair_types_2013_inter,
                self.affair_types_2014_inter,
                self.affair_types_2015_inter,
                self.affair_types_2016_inter,
                self.affair_types_2017_inter,
                self.affair_types_2018_inter,
                self.affair_types_2019_inter,
                self.affair_types_2020_inter,
            ],
            "data_postu": [
                self.affair_types_2010_postu,
                self.affair_types_2011_postu,
                self.affair_types_2012_postu,
                self.affair_types_2013_postu,
                self.affair_types_2014_postu,
                self.affair_types_2015_postu,
                self.affair_types_2016_postu,
                self.affair_types_2017_postu,
                self.affair_types_2018_postu,
                self.affair_types_2019_postu,
                self.affair_types_2020_postu,
            ],
            "data_motio": [
                self.affair_types_2010_motio,
                self.affair_types_2011_motio,
                self.affair_types_2012_motio,
                self.affair_types_2013_motio,
                self.affair_types_2014_motio,
                self.affair_types_2015_motio,
                self.affair_types_2016_motio,
                self.affair_types_2017_motio,
                self.affair_types_2018_motio,
                self.affair_types_2019_motio,
                self.affair_types_2020_motio,
            ],
            "data_pmoti": [
                self.affair_types_2010_pmoti,
                self.affair_types_2011_pmoti,
                self.affair_types_2012_pmoti,
                self.affair_types_2013_pmoti,
                self.affair_types_2014_pmoti,
                self.affair_types_2015_pmoti,
                self.affair_types_2016_pmoti,
                self.affair_types_2017_pmoti,
                self.affair_types_2018_pmoti,
                self.affair_types_2019_pmoti,
                self.affair_types_2020_pmoti,
            ],
        }

        return Response(data)

class AnalysisParlamentInterpellationOW(APIView):

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # data querys
    notDesired = Affair.objects.filter(parlament=100, affair_type="INTER", discussion_desired=False).count()
    desiredSuccess = Affair.objects.filter(parlament=100, affair_type="INTER", discussion_desired=True, accepted=True).count()
    desiredDeclined = Affair.objects.filter(parlament=100, affair_type="INTER", discussion_desired=True, accepted=False).count()

    def get(self, request, format=None):
        data = {
            "labels": ["no discussion desired", "discussion desired; success", "discussion desired; declined",],
            "data_notDesired": [
                self.notDesired,
            ],
            "data_desiredSuccess": [
                self.desiredSuccess,
            ],
            "data_desiredDeclined": [
                self.desiredDeclined,
            ]
        }

        return Response(data)

class AnalysisParlamentPostulateOW(APIView):
    # recommendation

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # data querys
    notRecommendedSuccess =Affair.objects.filter(parlament=100, affair_type="POSTU", recommendation=False, accepted=True).count()
    notRecommendedDeclined = Affair.objects.filter(parlament=100, affair_type="POSTU", recommendation=False, accepted=False).count()
    recommendedSuccess = Affair.objects.filter(parlament=100, affair_type="POSTU", recommendation=True, accepted=True).count()
    recommendedDeclined = Affair.objects.filter(parlament=100, affair_type="POSTU", recommendation=True, accepted=False).count()


    def get(self, request, format=None):
        data = {
            "labels": [
                "negative recommendation + accepted", 
                "negative recommendation + declined", 
                "positive recommendation + accepted", 
                "positive recommendation + declined",
            ],
            "data_notRecommendedSuccess": [
                self.notRecommendedSuccess,
            ],
            "data_notRecommendedDeclined": [
                self.notRecommendedDeclined,
            ],
            "data_recommendedSuccess": [
                self.recommendedSuccess,
            ],
            "data_recommendedDeclined": [
                self.recommendedDeclined,
            ],
        }

        return Response(data)

class AnalysisParlamentMotionOW(APIView):
    # recommendation

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # data querys
    notRecommendedSuccess =Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=False, recommendation=False, accepted=True).count()
    notRecommendedDeclined = Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=False, recommendation=False, accepted=False).count()
    
    recommendedSuccess = Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=False, recommendation=True, accepted=True).count()
    recommendedDeclined = Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=False, recommendation=True, accepted=False).count()
    
    transformationSuccess = Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=True, accepted=True).count()
    transformationDeclined = Affair.objects.filter(parlament=100, affair_type="MOTIO", transformation_recommendation=True, accepted=False).count()


    def get(self, request, format=None):
        data = {
            "labels": [
                "negative recommendation + accepted", 
                "negative recommendation + declined", 
                "positive recommendation + accepted", 
                "positive recommendation + declined",
                "transformation recommendation + accepted",
                "transformation recommendation + declined"
            ],
            "data_notRecommendedSuccess": [
                self.notRecommendedSuccess,
            ],
            "data_notRecommendedDeclined": [
                self.notRecommendedDeclined,
            ],
            "data_recommendedSuccess": [
                self.recommendedSuccess,
            ],
            "data_recommendedDeclined": [
                self.recommendedDeclined,
            ],
            "data_transformationSuccess": [
                self.transformationSuccess,
            ],
            "data_transformationDeclined": [
                self.transformationDeclined,
            ],
        }

        return Response(data)

class AnalysisParlamentPoliticansXXXOW(APIView):
    # success rate
    # mean of affairs
    # number of debate statements

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = {

        }

        return Response(data)