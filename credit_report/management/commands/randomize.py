import urllib.request
from datetime import datetime, timezone
from random import randint, choice, random, uniform, randrange
from typing import List

from credit_report.management.commands.populatedb import RATINGS, FINANCIALS, RISK_DRIVERS, RISK_DRIVER_DATA
from credit_report.management.commands.models import create_company, create_credit_report, create_financials_report, \
    create_financials, create_risk_driver, create_risk_driver_data
from credit_report.models import Company, FinancialsReport, RiskDriver, Unit


def random_companies(number_of_companies: int, from_year: int, to_year: int):
    companies = []
    with urllib.request.urlopen('http://www.desiquintans.com/downloads/nounlist/nounlist.txt') as response:
        nouns = response.read().decode().splitlines()
        print(f'Using {len(nouns)} nouns to create {number_of_companies} companies:')
        for i in range(number_of_companies):
            company, created = create_company(
                name=f'{choice(nouns)} {choice(nouns)} {choice(nouns)}',
            )
            if created:
                companies.append(company)
                random_credit_reports(company=company, from_year=from_year, to_year=to_year, )
    print(f'{len(companies)} companies created, {number_of_companies - len(companies)} duplicates')


def random_credit_reports(company: Company, from_year: int, to_year: int):
    financials_reports: List[FinancialsReport] = []
    for year in range(from_year, to_year + 1):
        report_date = datetime(year=year, month=1, day=1, tzinfo=timezone.utc)

        financials_report = create_financials_report(company=company, financials_report_date=report_date, )

        random_financials(financials_report=financials_report)
        random_risk_drivers(financials_report=financials_report)

        financials_reports.append(financials_report)

        create_credit_report(company=company, credit_report_score=randint(1, 1000),
                             credit_report_rating=choice(RATINGS), credit_report_date=report_date,
                             financials_reports=financials_reports, )


def random_financials(financials_report: FinancialsReport):
    for name, unit in FINANCIALS:
        create_financials(financials_report=financials_report, name=name, unit=unit, value=random_value(unit))


def random_risk_drivers(financials_report: FinancialsReport):
    for category, unit in RISK_DRIVERS:
        risk_driver = create_risk_driver(financials_report=financials_report, category=category, unit=unit)
        random_risk_driver_data(risk_driver=risk_driver, unit=unit)


def random_risk_driver_data(risk_driver: RiskDriver, unit: Unit):
    for name in RISK_DRIVER_DATA:
        create_risk_driver_data(risk_driver=risk_driver, name=name, value=random_value(unit))


def random_value(unit: Unit) -> float:
    value = 1
    if unit is Unit.PERCENTAGE:
        value = random()
    elif unit is Unit.MULTIPLICATIVE:
        value = uniform(0, 1000)
    elif unit is Unit.CURRENCY:
        value = uniform(0, 999_999_999_999)
    elif unit is Unit.UNKNOWN:
        value = randrange(999_999_999_999)
    return value
