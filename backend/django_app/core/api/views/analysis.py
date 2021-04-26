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

    authentication_classes = [JWTCookieAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # type count
    motions = Affair.objects.filter(parlament=100, affair_type="MOTIO").count()
    people_motions = Affair.objects.filter(parlament=100, affair_type="PMOTI").count()
    postulates = Affair.objects.filter(parlament=100, affair_type="POSTU").count()
    interpellations = Affair.objects.filter(parlament=100, affair_type="INTER").count()
    inquiries = Affair.objects.filter(parlament=100, affair_type="INQUI").count()


    def get(self, request, format=None):
        data = {
            "labels": ["Motions", "People Motions", "Postulates", "Interpellations", "Inquiries"],
            "data_all": [
                self.motions, self.people_motions, self.postulates, self.interpellations, self.inquiries,
            ],
        }

        return Response(data)