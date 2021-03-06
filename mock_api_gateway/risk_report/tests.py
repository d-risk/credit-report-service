from uuid import uuid4

from django.test import TestCase
from django.utils.timezone import now

from mock_api_gateway.risk_rating.models import RiskRating
from mock_api_gateway.risk_report.models import RiskReport


# Create your tests here.
class RiskReportTestCase(TestCase):
    def test_create_risk_report(self):
        company_id = uuid4()
        risk_score = 0.1
        risk_rating = RiskRating.AAA.readable_name
        date_time = now()

        risk_report = RiskReport.objects.create(
            company_id=company_id,
            risk_score=risk_score,
            risk_rating=risk_rating,
            date_time=date_time,
        )

        self.assertEqual(RiskReport.objects.count(), 1)
        self.assertIsNotNone(risk_report)
        self.assertEqual(risk_report.company_id, company_id)
        self.assertEqual(risk_report.risk_score, risk_score)
        self.assertEqual(risk_report.date_time, date_time)
