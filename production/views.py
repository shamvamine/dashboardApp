import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .models import fin_costs, fin_cost_budgets
from django.utils import timezone
from django.db.models import Sum, Avg
from .forms import *
import json
import calendar
from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from django import template
from datetime import date

register = template.Library()

@register.filter
def kg_to_oz(value):
    ounces = value * 32.1507
    return round(ounces, 3)


def get_latest_data_month_year():
    """
    Fetch the latest date from the Data model.
    If no data exists, return the current month and year.
    """
    latest_data = Data.objects.order_by('-date').first()
    
    if latest_data:
        # Use the date of the latest entry in Data model to determine the current month and year
        latest_date = latest_data.date
        current_month = latest_date.month
        current_year = latest_date.year
        current_month_name = calendar.month_name[current_month]
    else:
        # If no entries exist, use the current date as fallback
        current_date = timezone.now()
        current_month = current_date.month
        current_year = current_date.year
        current_month_name = calendar.month_name[current_month]
    
    return current_month, current_year, current_month_name



# Create your views here.

def getSafetyData():                                                        #safety perfomance data view - get all data related to the safety performance model for display
    # Get the current month and year
    current_date = timezone.now()
    # current_month = current_date.month
    # current_month_name = calendar.month_name[current_month]
    # current_year = current_date.year   
    current_month, current_year, current_month_name = get_latest_data_month_year()

    start_of_year = current_date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    data_ytd = SafetyPerformance.objects.filter(date__gte=start_of_year, date__lte=current_date)

    # Aggregate metrics for YTD
    fatality_ytd = data_ytd.aggregate(Sum('fatality'))['fatality__sum']
    lti_ytd = data_ytd.aggregate(Sum('lti'))['lti__sum']
    nlti_ytd = data_ytd.aggregate(Sum('nlti'))['nlti__sum']

    
    #get MTD values for the Safety Performance
    data = SafetyPerformance.objects.filter(date__month=current_month, date__year=current_year)

    fatality_mtd            = data.aggregate(Sum('fatality'))['fatality__sum']
    lti_mtd                 = data.aggregate(Sum('lti'))['lti__sum']   
    nlti_mtd                = data.aggregate(Sum('nlti'))['nlti__sum']

    mtd_summary = {
        'current_month'    : current_month_name,
        'fatality_mtd'     : fatality_mtd,
        'lti_mtd'          : lti_mtd,
        'nlti_mtd'         : nlti_mtd,
        'fatality_ytd'     : fatality_ytd,
        'lti_ytd'          : lti_ytd,
        'nlti_ytd'         : nlti_ytd
    }
    # print(mtd_summary)
    return mtd_summary

def getMTDs():
    # Get the current month and year
    # current_date = timezone.now()
    # current_month = current_date.month
    # current_month_name = calendar.month_name[current_month]
    # current_year = current_date.year 
    # 
    current_month, current_year, current_month_name = get_latest_data_month_year()  

    # Filter Summaries objects for the current month
    mtd_summaries = Data.objects.filter(date__month=current_month, date__year=current_year)
    
    if mtd_summaries.exists():
        # Calculate MTD values if data exists
        ug_tonnes = mtd_summaries.aggregate(Sum('ug_tonnes'))['ug_tonnes__sum'] or 0
        op_tonnes = mtd_summaries.aggregate(Sum('op_tonnes'))['op_tonnes__sum'] or 0
        milled_tonnes = mtd_summaries.aggregate(Sum('milled_tonnes'))['milled_tonnes__sum'] or 0
        dev_drilling = mtd_summaries.aggregate(Sum('dev_drilling'))['dev_drilling__sum'] or 0
        ore_gen = mtd_summaries.aggregate(Sum('ore_gen'))['ore_gen__sum'] or 0
        gold = mtd_summaries.aggregate(Sum('gold'))['gold__sum'] or 0
        grade = mtd_summaries.aggregate(Sum('grade'))['grade__sum'] or 0
        
        # For reconciled grade, consider only non-zero values
        non_zero_reconciled_grades = mtd_summaries.filter(reconciled_grade__gt=0)
        
        if non_zero_reconciled_grades.exists():
            # Calculate the sum and count of non-zero reconciled grades
            reconciled_grade_sum = non_zero_reconciled_grades.aggregate(Sum('reconciled_grade'))['reconciled_grade__sum'] or 0
            reconciled_grade_count = non_zero_reconciled_grades.count()

            # Calculate average reconciled grade (avoid division by zero)
            reconciled_grade = reconciled_grade_sum / reconciled_grade_count if reconciled_grade_count > 0 else 0
        else:
            reconciled_grade = 0
    else:
        # If no data exists, set all metrics to 0
        ug_tonnes, op_tonnes, milled_tonnes, dev_drilling, ore_gen, gold, grade, reconciled_grade = 0, 0, 0, 0, 0, 0, 0, 0
    
    # Pass MTD values to the template
    mtd_summary = {
        'current_month': current_month,
        'rom': ug_tonnes + op_tonnes,
        'milled_tonnes': milled_tonnes,
        'dev_drilling': dev_drilling,
        'ore_gen': ore_gen,
        'gold': round((float(gold) * 32.1507), 3),
        'grade': float(grade),
        'reconciled_grade': round(float(reconciled_grade), 3)
    }
    
    return mtd_summary



# def getMTDs():

#      # Get the current month and year
#     current_date            = timezone.now()
#     current_month           = current_date.month
#     current_month_name      = calendar.month_name[current_month]
#     current_year            = current_date.year   

#     # Filter Summaries objects fordef getMTDs():
#     # Get the current month and year
#     current_date = timezone.now()
#     current_month = current_date.month
#     current_month_name = calendar.month_name[current_month]
#     current_year = current_date.year   

#     # Filter Summaries objects for the current month
#     mtd_summaries = Data.objects.filter(date__month=current_month, date__year=current_year)
    
#     if mtd_summaries.exists():
#         # Calculate MTD values if data exists
#         ug_tonnes = mtd_summaries.aggregate(Sum('ug_tonnes'))['ug_tonnes__sum'] or 0
#         op_tonnes = mtd_summaries.aggregate(Sum('op_tonnes'))['op_tonnes__sum'] or 0
#         milled_tonnes = mtd_summaries.aggregate(Sum('milled_tonnes'))['milled_tonnes__sum'] or 0
#         dev_drilling = mtd_summaries.aggregate(Sum('dev_drilling'))['dev_drilling__sum'] or 0
#         ore_gen = mtd_summaries.aggregate(Sum('ore_gen'))['ore_gen__sum'] or 0
#         gold = mtd_summaries.aggregate(Sum('gold'))['gold__sum'] or 0
#         grade = mtd_summaries.aggregate(Sum('grade'))['grade__sum'] or 0
#         # reconciled_grade = mtd_summaries.aggregate(Sum('reconciled_grade'))['reconciled_grade__sum'] or 0
#          # For reconciled grade, consider only non-zero values
#         non_zero_reconciled_grades = mtd_summaries.filter(reconciled_grade__gt=0)
        
#         if non_zero_reconciled_grades.exists():
#             # Calculate the sum and count of non-zero reconciled grades
#             reconciled_grade_sum = non_zero_reconciled_grades.aggregate(Sum('reconciled_grade'))['reconciled_grade__sum'] or 0
#             reconciled_grade_count = non_zero_reconciled_grades.count()

#             # Calculate average reconciled grade (avoid division by zero)
#             reconciled_grade = reconciled_grade_sum / reconciled_grade_count if reconciled_grade_count > 0 else 0
#         else:
#             reconciled_grade = 0
#     else:
#         # If no data exists, set all metrics to 0
#         ug_tonnes, op_tonnes, milled_tonnes, dev_drilling, ore_gen, gold, grade = 0, 0, 0, 0, 0, 0, 0
    
#     # Pass MTD values to the template
#     mtd_summary = {
#         'current_month': current_month,
#         'rom': ug_tonnes + op_tonnes,
#         'milled_tonnes': milled_tonnes,
#         'dev_drilling': dev_drilling,
#         'ore_gen': ore_gen,
#         'gold': round((float(gold) * 32.1507), 3),
#         'grade': float(grade),
#         'reconciled_grade': round(float(reconciled_grade),3)
#     }
    
#     return mtd_summary 

def newGradeData():
    currentDate             = datetime.date.today()
    current_month, current_year, current_month_name = get_latest_data_month_year()
    # Retrieve monthly planned grade
    monthly_plan            = plan.objects.filter(date__year=current_year, date__month=current_month).first()

    # Retrieve daily grade data for the current month
    daily_data              = Data.objects.filter(date__year=current_year, date__month=current_month).values_list('date', 'grade').order_by('date')
    cil_data                = Data.objects.filter(date__year=current_year, date__month=current_month).values_list('date', 'cil_feed_grade').order_by('date')
    rec_data                = Data.objects.filter(date__year=current_year, date__month=current_month).values_list('date', 'reconciled_grade').order_by('date')

    # Prepare data for Chart.js format
    dates                   = [date.strftime('%b %d') for date, _ in daily_data]
    # dt                      = [date.strftime('%b %d') for date in daily_data if date.month == current_month and data.date.year == current_year]
    daily_grades            = [float(grade) for _, grade in daily_data]
    daily_cil               = [float(cil_feed_grade) for _, cil_feed_grade in cil_data]
    daily_reconc            = [float(reconciled_grade) for _, reconciled_grade in rec_data]
    monthly_plan_grade      = float(monthly_plan.grade) if monthly_plan else None


    # Create barChartData dictionary
    barChartData = {
        'dates'             : dates,
        'actual'            : daily_grades,
        'cil'               : daily_cil,
        'reconciled'        : daily_reconc,
        'grade'             : [monthly_plan_grade] * len(dates) if monthly_plan_grade else [None] * len(dates)
    }

    # Convert barChartData to JSON response
    chart_data_json         = json.dumps(barChartData)

    # print(chart_data_json,'json stuff')
    
    return chart_data_json

def romValues():
    currentDate             = datetime.date.today()
    current_month, current_year, current_month_name = get_latest_data_month_year()

    ug_data                 = Data.objects.filter(date__year=current_year, date__month=current_month).values_list('date', 'ug_tonnes').order_by('date')
    op_data                 = Data.objects.filter(date__year=current_year, date__month=current_month).values_list('date', 'op_tonnes').order_by('date')


    

    dates                   = [date.strftime('%b %d') for date, _ in ug_data]
    
    daily_ug_data           = [float(ug_tonnes) for _, ug_tonnes in ug_data]
    daily_op_data           = [float(op_tonnes) for _, op_tonnes in op_data]


    romChartData = {
        'dates'             : dates,
        'ug_data'           : daily_ug_data,
        'op_data'           : daily_op_data,
       }
    # print(barChartData)
    # Convert barChartData to JSON response
    rom_chart_data_json         = json.dumps(romChartData)

    # print(chart_data_json,'json stuff')
    
    return rom_chart_data_json

def get_plan_for_current_month():
    # Get the current month and year
    # current_date                = timezone.now()
    # current_month               = current_date.month
    # current_month_name          = calendar.month_name[current_month]
    # current_year                = current_date.year   

    current_month, current_year, current_month_name = get_latest_data_month_year()

    # Query the budgets model for records matching the current month and year
    budget_record               = plan.objects.filter(date__month=current_month, date__year=current_year).first()
    
    if budget_record:
        # # If record exists for the current month, return the record
        # return budget_record.values()
        # Convert gold value from kilograms to ounces
        budget_record_dict = {
            'date'              : budget_record.date,
            'rom'               : budget_record.rom,
            'milled_tonnes'     : budget_record.milled_tonnes,
            'gold'              : round((budget_record.gold * 32.1507), 4), # Convert kg to oz
            'grade'             : budget_record.grade,
            'dev_drilling'      : budget_record.dev_drilling,
            'ore_gen'           : budget_record.ore_gen,
            'recovery'          : budget_record.recovery,
            'month_name'        : current_month_name,
        }
        return budget_record_dict
    else:
        # If no record exists, return a default record with all values set to 0
        return {
            'date'              : timezone.now(),
            'rom'               : 0,
            'milled_tonnes'     : 0,
            'gold'              : 0,
            'grade'             : 0,
            'dev_drilling'      : 0,
            'ore_gen'           : 0,
            'recovery'          : 0,
            'month_name'        : current_month_name,
        }

def get_budget_for_current_month():
    # Get the current month and year
    # current_date                = timezone.now()
    # current_month               = current_date.month
    # current_month_name          = calendar.month_name[current_month]
    # current_year                = current_date.year  
    current_month, current_year, current_month_name = get_latest_data_month_year() 

    # Query the budgets model for records matching the current month and year
    budget_record               = budget.objects.filter(date__month=current_month, date__year=current_year).first()
    
    if budget_record:
        # # If record exists for the current month, return the record
        # return budget_record.values()
        # Convert gold value from kilograms to ounces
        budget_record_dict = {
            'date'              : budget_record.date,
            'rom'               : budget_record.rom,
            'milled_tonnes'     : budget_record.milled_tonnes,
            'gold'              : round((budget_record.gold * 32.1507), 4), # Convert kg to oz
            'grade'             : budget_record.grade,
            'dev_drilling'      : budget_record.dev_drilling,
            'ore_gen'           : budget_record.ore_gen,
            'recovery'          : budget_record.recovery,
            'month_name'        : current_month_name,
        }
        return budget_record_dict
    else:
        # If no record exists, return a default record with all values set to 0
        return {
            'date'              : timezone.now(),
            'rom'               : 0,
            'milled_tonnes'     : 0,
            'gold'              : 0,
            'grade'             : 0,
            'dev_drilling'      : 0,
            'ore_gen'           : 0,
            'recovery'          : 0,
            'month_name'        : current_month_name,
        }

def get_mtd_deltas():
    # Get the current date, month, and year
    current_date = timezone.now().date()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day

    # Calculate the previous month and year
    if current_month == 1:
        prev_month = 12
        prev_year = current_year - 1
    else:
        prev_month = current_month - 1
        prev_year = current_year

    # Get records for the current month up to the current date
    current_month_records = Data.objects.filter(
        date__year=current_year,
        date__month=current_month,
        date__day__lte=current_day
    )

    # Get records for the previous month up to the same date
    prev_month_records = Data.objects.filter(
        date__year=prev_year,
        date__month=prev_month,
        date__day__lte=current_day
    )

    # Calculate MTD sums for current month
    current_mtd = current_month_records.aggregate(
        ug_tonnes_sum=Sum('ug_tonnes'),
        op_tonnes_sum=Sum('op_tonnes'),
        milled_tonnes_sum=Sum('milled_tonnes'),
        dev_drilling_sum=Sum('dev_drilling'),
        ore_gen_sum=Sum('ore_gen'),
        gold_sum=Sum('gold')
    )

    # Calculate MTD sums for previous month
    prev_mtd = prev_month_records.aggregate(
        ug_tonnes_sum=Sum('ug_tonnes'),
        op_tonnes_sum=Sum('op_tonnes'),
        milled_tonnes_sum=Sum('milled_tonnes'),
        dev_drilling_sum=Sum('dev_drilling'),
        ore_gen_sum=Sum('ore_gen'),
        gold_sum=Sum('gold')
    )

    # Handle None values by setting them to 0
    current_mtd = {key: value or 0 for key, value in current_mtd.items()}
    prev_mtd = {key: value or 0 for key, value in prev_mtd.items()}

    # Calculate deltas
    deltas = {
        'ug_tonnes_delta': round(current_mtd['ug_tonnes_sum'] - prev_mtd['ug_tonnes_sum'], 4),
        'op_tonnes_delta': round(current_mtd['op_tonnes_sum'] - prev_mtd['op_tonnes_sum'], 4),
        'milled_tonnes_delta': round(current_mtd['milled_tonnes_sum'] - prev_mtd['milled_tonnes_sum'], 4),
        'dev_drilling_delta': round(current_mtd['dev_drilling_sum'] - prev_mtd['dev_drilling_sum'], 4),
        'ore_gen_delta': round(current_mtd['ore_gen_sum'] - prev_mtd['ore_gen_sum'], 4),
        'gold_delta': round(current_mtd['gold_sum'] - prev_mtd['gold_sum'], 4)
    }

    return deltas

def get_daily_deltas():
    # Get the latest date (last recorded date) from the table
    current_record = Data.objects.order_by('-date').first()

    if not current_record:
        # Handle the case when there are no records
        return None

    # Get the record for the day before the latest record
    prev_record                     = Data.objects.filter(date__lt=current_record.date).order_by('-date').first()

    if not prev_record:
        # Handle the case when there is no previous record (e.g., only one record exists)
        return None
    
    # Find the latest non-zero gold record
    latest_non_zero_gold_record     = Data.objects.filter(gold__gt=0).order_by('-date').first()

    # Initialize gold_delta in case we can't calculate it
    gold_delta = None

    if latest_non_zero_gold_record:
        # Find the previous non-zero gold record
        previous_non_zero_gold_record = Data.objects.filter(gold__gt=0, date__lt=latest_non_zero_gold_record.date).order_by('-date').first()

        if previous_non_zero_gold_record:
            # Calculate gold delta between the latest and previous non-zero values
            gold_delta          = round(latest_non_zero_gold_record.gold - previous_non_zero_gold_record.gold, 4)
        else:
            # If only one non-zero value exists, use that for the month (no delta comparison)
            gold_delta          = round(latest_non_zero_gold_record.gold, 4)

    # Calculate the deltas between the last recorded day and the previous day
    deltas = {
        'ug_tonnes_delta'       : round(current_record.ug_tonnes - prev_record.ug_tonnes, 4),
        'op_tonnes_delta'       : round(current_record.op_tonnes - prev_record.op_tonnes, 4),
        'milled_tonnes_delta'   : round(current_record.milled_tonnes - prev_record.milled_tonnes, 4),
        'dev_drilling_delta'    : round(current_record.dev_drilling - prev_record.dev_drilling, 4),
        'ore_gen_delta'         : round(current_record.ore_gen - prev_record.ore_gen, 4),
        'gold_delta'            : gold_delta if gold_delta is not None else round(current_record.gold - prev_record.gold, 4),
        'grade_delta'           : current_record.reconciled_grade - prev_record.reconciled_grade,
    }

    print('curr', current_record.grade, 'prev', prev_record.grade)

    return deltas


def getData(request):
    # current_date                = timezone.now()
    # current_month               = current_date.month
    # current_month_name          = calendar.month_name[current_month]
    # current_year                = current_date.year  

    current_month, current_year, current_month_name = get_latest_data_month_year()

    delta_values                = get_daily_deltas()
    

    prod_data                   = Data.objects.all().order_by('-date').first()
    # Check if prod_data is not None
    if prod_data:
        # Convert gold value from kg to oz
        gold_oz                 = float(prod_data.gold) * 32.1507

        # Update the prod_data object with the gold value in ounces
        prod_data.gold          = round(gold_oz,3)
        
   
    Plan                        = get_plan_for_current_month()

    Budget                      = get_budget_for_current_month()

    PerSummary                  = getSafetyData()            # safety performance data summary 

    mtd_data                    = getMTDs()                  # Month to date values


    # Fetch data from the Production_Data model
    production_data             = Data.objects.all().order_by('date')

    # Extracting data for the chart
    # Filter the production data for dates in the current month
    current_month_data          = [data.date.strftime('%b %d') for data in production_data if data.date.month == current_month and data.date.year == current_year]
   
    dates                       = [data.date.strftime('%b %d') for data in production_data]
    
    milled_tonnage              = [data.milled_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]
    ug_tonnage                  = [data.ug_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]
    op_tonnage                  = [data.op_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]
    stock_pile                  = [data.stock_pile for data in production_data if data.date.month == current_month and data.date.year == current_year]

    # Calculate ROM tonnage (ug_tonnes + op_tonnes)
    rom                         = [ug + op for ug, op in zip(ug_tonnage, op_tonnage)]

    rom_chart_data              = romValues()

    # print(rom_chart_data)

    cost_data                   = fin_costs.objects.all().order_by('-date').first()

    chart_data = {
        
        'dates'                  : current_month_data,       
        'milled_tonnage'         : milled_tonnage,
        'rom'                    : rom,
        'stock_pile'             : stock_pile
    }

 
    chart_data_json             = json.dumps(chart_data)
    

    # Get the current date
    current_date                = timezone.now().date()

    # Get the latest record where lti is greater than 0
    last_lti_record             = SafetyPerformance.objects.filter(lti__gt=0).order_by('-date').first()

    # Check if there is a record with an lti
    if last_lti_record:
        # Calculate the difference in days between the current date and the date of the last lti
        days_since_last_lti     = (current_date - last_lti_record.date).days
    else:
        # If no record exists, return None or a default value
        days_since_last_lti     = 0

    
    bar_chart_data_json         = newGradeData()
    # print(bar_chart_data_json,'some json stuff too')
    # bar_chart_data_json = json.dumps(newGradeData())

    def calculate_percentage(plan_value, actual_value):
        if plan_value > 0:
            return ((plan_value - actual_value) / plan_value) * 100
        return 0
    
    percentages_remaining = {
        'rom'                   : calculate_percentage(Plan['rom'] if Plan else 0, mtd_data['rom'] if mtd_data else 0),
        'milled_tonnes'         : calculate_percentage(Plan['milled_tonnes'] if Plan else 0, mtd_data['milled_tonnes'] if mtd_data else 0),
        'ore_gen'               : calculate_percentage(Plan['ore_gen'] if Plan else 0, mtd_data['ore_gen'] if mtd_data else 0),
        'gold'                  : calculate_percentage(Plan['gold'] if Plan else 0, mtd_data['gold'] if mtd_data else 0),
    }

    print('Planned Recovery: ', plan.recovery)

    context = {

        'summary'               : prod_data,
        'costs'                 : cost_data,
        'deltas'                : delta_values,
        'perfomance'            : PerSummary,
        'plan'                  : Plan,
        'budget'                : Budget,
        'mtd'                   : mtd_data,
        'chart_data'            : chart_data_json,
        'bar_chart_data'        : bar_chart_data_json,
        'rom_chart_data'        : rom_chart_data,
        'percentages_remaining' : percentages_remaining,
        'days_since_last_lti'   : days_since_last_lti,
        
        

    }
    return render(request, 'home/index.html', context)


def get_costs_dash(request):
    current_date                = timezone.now()
    current_month               = current_date.month
    current_month_name          = calendar.month_name[current_month]
    current_year                = current_date.year  

    # Filter data for the current month and year
    spendings                   = dept_spending.objects.filter(date__month=current_month, date__year=current_year)

    # Fetch budget data for the current month and year
    budgets                     = fin_budgets.objects.filter(date__month=current_month, date__year=current_year)
    budgets_dict                = {budget.department.id: budget.total_c1_cost for budget in budgets}

    # Fetch plan data for the current month and year
    plans                       = dept_spending_plan.objects.filter(date__month=current_month, date__year=current_year)
    plans_dict                  = {plan.department.id: plan.total_c1_cost for plan in plans}

    # Aggregate data by department
    departments                 = []
    actual_spends               = []
    planned_spends              = []
    labels                      = []

    for spending in spendings:
        dept_id                 = spending.department.id
        dept_data               = {
            'name'              : spending.department.name,
            'total_c1_cost'     : spending.total_c1_cost,
            'budget'            : budgets_dict.get(dept_id, 0),
            'plan'              : plans_dict.get(dept_id, 0),
            'actual'            : spending.total_c1_cost
        }
        departments.append(dept_data)
        labels.append(spending.department.name)
        actual_spends.append(float(spending.total_c1_cost))
        planned_spends.append(float(plans_dict.get(dept_id, 0)))

    if spendings:
        bData = {
            'labels': labels,
            'spend': actual_spends,
            'plan': planned_spends,
        }
    else:
        bData = {
            'labels': [],
            'spend': [],
            'plan': [],
        }

    barData = json.dumps(bData)

    context = {
        'title': 'Costs Dashboard',
        'head': 'Spending Analysis for each department',
        'current_month': current_month_name,
        'departments': departments,
        'labels': labels,
        'actual_spends': actual_spends,
        'planned_spends': planned_spends,
        'barData': barData,
    }

    return render(request, 'home/costs_dashboard.html', context)

@login_required
def safetyPrformance(request):
    list                        = SafetyPerformance.objects.all().order_by('-date')

    context                     = {
        'title'                 : 'Safety Performance',
        'head'                  : 'Safety Performance',
        'performanceList'       : list
    }

    return render (request, 'production/safetyPerformance.html', context)

@login_required
def addSafetyPerfData(request):
    if request.method == 'POST':
        form = SafertyPerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New record created succesfully.')
            messages.success(request,message)
            return redirect('sperformance-list')
    else:
        form = SafertyPerformanceForm()

    context = {
        'title'                 : 'Safety Performance',
        'head'                  :'Input Safety Performance Data',
        'form'                  : form

    }
    return render(request, 'production/addSafetyPerformanceData.html', context)

@login_required
def updateSafetyData(request, pk):
    data                            = get_object_or_404(SafetyPerformance, id=pk)
    if request.method               == 'POST':
        form = SafertyPerformanceForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, f'Data has been updated successfully. ')
            return redirect('sperformance-list')
    else:
        form = SafertyPerformanceForm(instance=data)

    context = {
        'title'                 : 'Update Safety Performance Data',
        'head'                  : 'Update Safety Performance Data',
        'form'                  : form,
        'data_id'               : pk
    }

    return render(request, 'production/updateSafetyPer.html', context)

@login_required
def summaries_list(request):
    list = Data.objects.all().order_by('-date')
    context = {
        'title'                 : 'Production Data',
        'head'                  : 'Data',
        'summaryList'           : list
    }
    return render(request, 'production/summariesList.html', context)


@login_required
def input_data(request):    
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New record created succesfully.')
            messages.success(request,message)
            return redirect('summaries-list')
    else:
        form = DataForm()

    context = {
        'title'                 : 'Input Data',
        'head'                  :'Input Data',
        'form'                  : form

    }
    return render(request, 'production/input.html', context)

@login_required
def update_data(request, pk):
    data                            = get_object_or_404(Data, id=pk)
    if request.method               == 'POST':
        form = DataForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, f'Data has been updated successfully. ')
            return redirect('summaries-list')
    else:
        form = DataForm(instance=data)

    context = {
        'title'                 : 'Update Production Data',
        'head'                  : 'Update Production Data',
        'form'                  : form,
        'data_id'               : pk
    }

    return render(request, 'production/updateData.html', context)

@login_required
def target_data(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('targets')
    else:
        form = PlanForm()
    
    context = {
        'title'             : 'Target Data Input',
        'head'              : 'Target Data Input',
        'form'              : form
    }
    return render(request, 'production/addTargets.html', context)

@login_required
def target_data_list(request):
    target_data = plan.objects.all()
    context = {
        'title'             : 'Monthly Targets',
        'head'              : 'Targets',
        'targetData'        : target_data
    }

    return render(request, 'production/targets.html', context)

@login_required
def updateTargetData(request, pk):
    data                            = get_object_or_404(plan, id=pk)
    if request.method               == 'POST':
        form = PlanForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, f'Data has been updated successfully. ')
            return redirect('targets')
    else:
        form = PlanForm(instance=data)

    context = {
        'title'         : 'Update Targets Data',
        'head'          : 'Update Targets Data',
        'form'          : form,
        'data_id'       : pk
    }

    return render(request, 'production/updateTargets.html', context)


@login_required
def budget_data_list(request):
    budget_data = budget.objects.all()
    context = {
        'title'             : 'Monthly Budgets',
        'head'              : 'Budgets',
        'BudgetData'        :  budget_data
    }

    return render(request, 'production/productionBudget.html', context)

@login_required
def add_budget_data(request):
    if request.method == 'POST':
        form = BudgetsForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('budgets-list')
    else:
        form = BudgetsForm()
    
    context = {
        'title'             : 'Budget Data Input',
        'head'              : 'Budget Data Input',
        'form'              : form
    }
    return render(request, 'production/addProductionBudget.html', context)
##ad budgets information


@login_required
def cost_budgets_list(request):
    data                    = fin_cost_budgets.objects.all()

    context                 = {
        'title'             : 'Cost Budgets',
        'head'              : 'Budgets',
        'budgetsData'       : data
    }

    return render(request, 'production/costBudgets.html', context)

@login_required
def add_cost_budget(request):
    if request.method == 'POST':
        form = FinCostsBudgetsForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('cost-budget-list')
    else:
        form = FinCostsBudgetsForm()
    
    context = {
        'title'             :'Budget Data Input',
        'head'              : 'Cost Budgets',
        'form'              : form
    }
    return render(request, 'production/addCostBudgets.html', context)

@login_required
def get_scats_tails(request):
    data                   = gold_estimate.objects.all()

    context                = {
        'title'            : 'CIL, Scats & GRG List',
        'head'             : 'CIL, Scats & GRG',
        'scatsData'        :  data

    }
    return render(request, 'production/scatsTailsList.html', context)

@login_required
def addScatsTails(request):
    if request.method == 'POST':
        form = GoldEstimateForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('scats-list')
    else:
        form = GoldEstimateForm()
    
    context = {
        'title'                 : 'CIL, Scats & GRG',
        'head'                  : 'Add CIL, Scats & GRG',
        'form'                  : form
    }
    return render(request, 'production/addScatsTails.html', context)

@login_required
def updateScatsTails(request, pk):
    data                            = get_object_or_404(gold_estimate, id=pk)
    if request.method               == 'POST':
        form = GoldEstimateForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, f'Data has been updated successfully. ')
            return redirect('scats-list')
    else:
        form = GoldEstimateForm(instance=data)

    context = {
        'title'         : 'Update Scats & Tails Data',
        'head'          : 'Update Scats & Tails Data',
        'form'          : form,
        'data_id'       : pk
    }

    return render(request, 'production/updateScatsTails.html', context)



# getting data for the cil-scats-grg graph
def cilScatsGrg_current_month():
    # Get the current month and year
    current_date = timezone.now()
    current_month = current_date.month
    current_year = current_date.year

    # Filter gold_estimate objects for the current month
    estimates = gold_estimate.objects.filter(date__year=current_year, date__month=current_month)

    if not estimates.exists():
        # If no records exist for the current month, return None or an empty dataset
        return {
            'cil': [],
            'scats': [],
            'grg': [],
            'dates': []
        }

   # Create float data points for each field (cil, scats, grg) and their respective dates
    cil_values = [float(entry.cil) for entry in estimates]
    scats_values = [float(entry.scats) for entry in estimates]
    grg_values = [float(entry.grg) for entry in estimates]
    dates = [entry.date.strftime("%d-%b-%Y") for entry in estimates]

    # Return the data as a dictionary
    data = {
        'cil': cil_values,
        'scats': scats_values,
        'grg': grg_values,
        'dates': dates
    }
    return data


def gold_estimate_details(request):
    # Get the current date
    # current_date = timezone.now()
    # current_month = current_date.month
    # current_year = current_date.year

    current_month, current_year, current_month_name = get_latest_data_month_year()

    # Filter records for the current month
    gold_records = gold_estimate.objects.filter(date__month=current_month, date__year=current_year)

    # Number of days recorded in the month
    days_recorded = gold_records.count() -2

    # Number of days remaining in the current month
    total_days_in_month = calendar.monthrange(current_year, current_month)[1]
    days_remaining = (total_days_in_month - days_recorded) - 2

    
    total_gold = sum(record.total for record in gold_records)

    # Average gold per day
    average_gold_per_day = total_gold / days_recorded if days_recorded > 0 else 0

    #get the gold forecast for the remaining days based on average gold per day
    remaining_gold = average_gold_per_day * days_remaining if days_recorded > 0 else 0

    #month end forcast
    forecast_gold = remaining_gold + total_gold

    
    graph_data = cilScatsGrg_current_month()

    chart_data_json             = json.dumps(graph_data)

    context = {
        'days_recorded': days_recorded,
        'days_remaining': days_remaining,
        'total_gold': round(total_gold,3),
        'average_gold_per_day': round(average_gold_per_day,3),
        'remaining_gold': round(remaining_gold,3),
        'forecast_gold': round(forecast_gold,3),
        'chartData': chart_data_json
        # 'dates': [date.strftime('%Y-%m-%d') for date in dates],  # Format dates as strings for JSON
        # 'daily_totals': daily_totals,
    }

    return render (request, 'production/gold_details.html', context)

#Function to be used in the following view for variance calculations
def calculate_variance(actual, budget):
    if budget is None or budget == 0:
        return None  # Handle division by zero
    return round(((actual - budget) / budget) * 100, 2)

def costs_details(request):

    # Get the current date, month, and year
    # current_date = timezone.now()
    # current_month = current_date.month
    # current_month_name = calendar.month_name[current_month]
    # current_year = current_date.year

    current_month, current_year, current_month_name = get_latest_data_month_year()

    # Retrieve cost data for the current month
    cost_data = fin_costs.objects.filter(date__month=current_month, date__year=current_year)
    dates = [data.date.strftime('%b %d') for data in cost_data]

    # Extract c1, c2, and c3 values from cost_data and convert to float
    c1_total = [float(cost.total_c1_cost) for cost in cost_data]
    c2_total = [float(cost.total_c2_cost) for cost in cost_data]
    c3_total = [float(cost.total_c3_cost) for cost in cost_data]
    c1_values = [float(cost.c1) for cost in cost_data]
    c2_values = [float(cost.c2) for cost in cost_data]
    c3_values = [float(cost.c3) for cost in cost_data]
    gold_price = [float(cost.gold_price) for cost in cost_data]

    # Calculate MTD values for actual costs
    mtd_data = fin_costs.objects.filter(date__month=current_month, date__year=current_year).aggregate(
        mtd_mining=Sum('mining'),
        mtd_mine_engineering=Sum('mine_engineering'),
        mtd_processing=Sum('processing'),
        mtd_hauling=Sum('hauling'),
        mtd_tsd=Sum('tsd'),
        mtd_owners=Sum('owners'),
        mtd_open_pit=Sum('open_pit'),
        mtd_depreciation=Sum('depreciation'),
        mtd_c3_cost=Sum('c3_cost'),
        mtd_total_c1=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit'),
        mtd_total_c2=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit') + Sum('depreciation'),
        mtd_total_c3=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit') + Sum('depreciation') + Sum('c3_cost'),
    )

    # Calculate MTD values for budget costs
    mtd_budgets_data = fin_cost_budgets.objects.filter(date__month=current_month, date__year=current_year).aggregate(
        mtd_budget_mining=Sum('mining'),
        mtd_budget_mine_engineering=Sum('mine_engineering'),
        mtd_budget_processing=Sum('processing'),
        mtd_budget_hauling=Sum('hauling'),
        mtd_budget_tsd=Sum('tsd'),
        mtd_budget_owners=Sum('owners'),
        mtd_budget_open_pit=Sum('open_pit'),
        mtd_budget_depreciation=Sum('depreciation'),
        mtd_budget_c3_cost=Sum('c3_cost'),
        mtd_budget_total_c1=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit'),
        mtd_budget_total_c2=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit') + Sum('depreciation'),
        mtd_budget_total_c3=Sum('mining') + Sum('mine_engineering') + Sum('processing') + Sum('hauling') + Sum('tsd') + Sum('owners') + Sum('open_pit') + Sum('depreciation') + Sum('c3_cost'),
    )

    # Calculate percentage variances
    variances = {
        'mining_variance': calculate_variance(mtd_data['mtd_mining'], mtd_budgets_data['mtd_budget_mining']),
        'mine_engineering_variance': calculate_variance(mtd_data['mtd_mine_engineering'], mtd_budgets_data['mtd_budget_mine_engineering']),
        'processing_variance': calculate_variance(mtd_data['mtd_processing'], mtd_budgets_data['mtd_budget_processing']),
        'hauling_variance': calculate_variance(mtd_data['mtd_hauling'], mtd_budgets_data['mtd_budget_hauling']),
        'tsd_variance': calculate_variance(mtd_data['mtd_tsd'], mtd_budgets_data['mtd_budget_tsd']),
        'owners_variance': calculate_variance(mtd_data['mtd_owners'], mtd_budgets_data['mtd_budget_owners']),
        'open_pit_variance': calculate_variance(mtd_data['mtd_open_pit'], mtd_budgets_data['mtd_budget_open_pit']),
        'depreciation_variance': calculate_variance(mtd_data['mtd_depreciation'], mtd_budgets_data['mtd_budget_depreciation']),
        'c3_cost_variance': calculate_variance(mtd_data['mtd_c3_cost'], mtd_budgets_data['mtd_budget_c3_cost']),
        'total_c1_variance': calculate_variance(mtd_data['mtd_total_c1'], mtd_budgets_data['mtd_budget_total_c1']),
        'total_c2_variance': calculate_variance(mtd_data['mtd_total_c2'], mtd_budgets_data['mtd_budget_total_c2']),
        'total_c3_variance': calculate_variance(mtd_data['mtd_total_c3'], mtd_budgets_data['mtd_budget_total_c3']),
    }

    # Preparing chart info
    costs_budgets = fin_cost_budgets.objects.filter(date__month=current_month, date__year=current_year)
    c1_budgets = [float(bud.total_c1_cost_budget) for bud in costs_budgets]
    c2_budgets = [float(bud.total_c2_cost_budget) for bud in costs_budgets]
    c3_budgets = [float(bud.total_c3_cost_budget) for bud in costs_budgets]

    price_chart_info = {
        'dates': dates,
        'c1_total': c1_total,
        'c2_total': c2_total,
        'c3_total': c3_total,
        'c1_budget': c1_budgets,
        'c2_budget': c2_budgets,
        'c3_budget': c3_budgets,
    }

    chart_info = {
        'dates': dates,
        'c1_values': c1_values,
        'c2_values': c2_values,
        'c3_values': c3_values,
        'gold_price': gold_price,
    }

    chart_info_json = json.dumps(chart_info)
    price_info_json = json.dumps(price_chart_info)

    context = {
        'title': 'Gold Analysis',
        'head': 'Gold',
        'cost_chart': chart_info_json,
        'price_chart': price_info_json,
        'mtd_data': mtd_data,
        'mtd_budget': mtd_budgets_data,
        'variances': variances,  # Add variances to the context
    }

    return render(request, 'production/costs_details.html', context)

def rom__details(request):
    # current_date            = timezone.now()
    # current_month           = current_date.month
    # current_month_name      = calendar.month_name[current_month]
    # current_year            = current_date.year  

    current_month, current_year, current_month_name = get_latest_data_month_year()

    Plan                    = get_budget_for_current_month()
    rom_value               = Plan['rom']
    mill_value              = Plan['milled_tonnes']

    # print(rom_value, 'Rom Value')

    days_in_current_month   = calendar.monthrange(current_year, current_month)[1]

    # Calculate the daily target
    daily_target            = round((rom_value / days_in_current_month),2)
    daily_mill_target       = round((mill_value/days_in_current_month),2)

    # Print the daily target
    # print(round(daily_target,2), 'Daily Target')

    rom_chart_data          = romValues()
    
    # print(rom_chart_data)
     # Fetch data from the Production_Data model
    production_data         = Data.objects.all().order_by('date')

    # Extracting data for the chart
    # Filter the production data for dates in the current month
    current_month_data       = [data.date.strftime('%b %d') for data in production_data if data.date.month == current_month and data.date.year == current_year]
   
    dates                    = [data.date.strftime('%b %d') for data in production_data]
    
    milled_tonnage           = [data.milled_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]
    ug_tonnage               = [data.ug_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]
    op_tonnage               = [data.op_tonnes for data in production_data if data.date.month == current_month and data.date.year == current_year]

    
    rom_plan                 = float(daily_target) if Plan else None
    mill_plan                = float(daily_mill_target) if Plan else None



    # Calculate ROM tonnage (ug_tonnes + op_tonnes)
    rom                     = [ug + op for ug, op in zip(ug_tonnage, op_tonnage)]

    rom_chart_data          = romValues()

    # print(rom_chart_data)

    chart_data = {
        
        'dates'                  : current_month_data,
        'rom_plan'               : [rom_plan] * len(dates) if rom_plan else [None] * len(dates),
        'mill_plan'              : [mill_plan] * len(dates) if mill_plan else [None] * len(dates),
        'milled_tonnage'         : milled_tonnage,
        'rom'                    : rom   
    }

 
    chart_data_json = json.dumps(chart_data)

    context = {

        'title'             : 'Run of Mine Analysis',
        'head'              : 'R.O.M',
        'rom_chart_data'    : rom_chart_data,
        'chart_data'        : chart_data_json,
        

    }
    # print('context',context)

    return render(request, 'production/rom_details.html', context)



def milling__details(request):

    context = {

        'title'             : 'Milling Analysis',
        'head'              : 'Milling',
        

    }

    return render(request, 'production/milling_details.html', context)

def ore_gen_details(request):
    # current_date            = timezone.now()
    # current_month           = current_date.month
    # current_month_name      = calendar.month_name[current_month]
    # current_year            = current_date.year 

    current_month, current_year, current_month_name = get_latest_data_month_year()

    # Retrieve cost data for the current month
    tramming_data           = trammings.objects.filter(date__month=current_month, date__year=current_year).order_by('date')
    dates                   = [data.date.strftime('%b %d') for data in tramming_data]

    western_top             = [tram.western_top for tram in tramming_data]
    western_top_grade       = [float(tram.western_top_grade) for tram in tramming_data]
    cymric_top              = [tram.cymric_top for tram in tramming_data]
    cymric_top_grade        = [float(tram.cymric_top_grade) for tram in tramming_data]
    cymric_bottom           = [tram.cymric_bottom for tram in tramming_data]
    cymric_bottom_grade     = [float(tram.cymric_bottom_grade) for tram in tramming_data]
    l_13                    = [tram.l_13 for tram in tramming_data]
    l_13_grade              = [float(tram.l_13_grade) for tram in tramming_data]
    l_15                    = [tram.l_15 for tram in tramming_data]
    l_15_grade              = [float(tram.l_15_grade) for tram in tramming_data]
    far_east                = [tram.far_east for tram in tramming_data]
    far_east_grade          = [float(tram.far_east_grade) for tram in tramming_data]


    chart_info = {
        'dates'                 : dates,
        'western_top'           : western_top,
        'western_top_grade'     : western_top_grade,
        'cymric_top'            : cymric_top,
        'cymric_top_grade'      : cymric_top_grade,
        'cymric_bottom'         : cymric_bottom,
        'cymric_bottom_grade'   : cymric_bottom_grade,
        'l_13'                  : l_13,
        'l_13_grade'            : l_13_grade,
        'l_15'                  : l_15,
        'l_15_grade'            : l_15_grade,
        'far_east'              : far_east,
        'far_east_grade'        : far_east_grade
    }

    chart_info_json = json.dumps(chart_info)

    context                 = {
        'title'             : 'Ore Generation Breakdown',
        'head'              : 'Ore Generation',
        'chart_data'        : chart_info_json

    }

    return render(request, 'production/tramming_details.html', context)


@login_required
def get_dept_spend_budget(request):
    data                    = fin_budgets.objects.all()

    context                 = {
        'title'             : 'Spending Budget',
        'head'              : 'Monthly Spending Analysis',
        'SpendingData'      : data


    }

    return render (request, 'production/deptSpendingBudgets.html', context)

@login_required
def get_dept_spend_plan(request):
    data                    = dept_spending_plan.objects.all()

    context                 = {
        'title'             : 'Spending Plan',
        'head'              : 'Monthly Spending Analysis',
        'SpendingData'      : data


    }

    return render (request, 'production/deptSpendingPlan.html', context)

@login_required
def add_dept_spending_plan(request):
    if request.method == 'POST':
        form = DeptSpendingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('dept-spend-plan')
    else:
        form = DeptSpendingPlanForm()
    
    context = {
        'title'                 : 'Department Spending Plan',
        'head'                  : 'Add Spending Plan',
        'form'                  : form
    }
    return render(request, 'production/addDeptSpendingPlan.html', context)

@login_required
def add_dept_spending_budget(request):
    if request.method == 'POST':
        form = DeptSpendingBudgetForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('dept-spend-budget')
    else:
        form = DeptSpendingBudgetForm()
    
    context = {
        'title'                 : 'Department Spending Budgets',
        'head'                  : 'Add Spending Budget',
        'form'                  : form
    }
    return render(request, 'production/addDeptSpendingBudget.html', context)

@login_required
def get_dept_spending(request):
    data                    = dept_spending.objects.all()

    context                 = {
        'title'             : 'Monthly Spend',
        'head'              : 'Monthly Spending Analysis',
        'SpendingData'      : data


    }

    return render (request, 'production/deptSpendingList.html', context)

@login_required
def add_dept_spending(request):
    if request.method == 'POST':
        form = DeptSpendingForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('spending-list')
    else:
        form = DeptSpendingForm()
    
    context = {
        'title'                 : 'Department Spending',
        'head'                  : 'Add Spending',
        'form'                  : form
    }
    return render(request, 'production/addDeptSpendingBudget.html', context)

@login_required
def cost_list(request):

    data                   = fin_costs.objects.all()

    context                = {
        'title'            : 'Costs List',
        'head'             : 'Costs',
        'CostsData'        :  data

    }

    return render (request, 'production/costs.html', context)


@login_required
def goldPriceList(request):
    data                    = GoldPrice.objects.all()
    context                 = {
        'title'             : 'Gold Price List',
        'head'              : 'Gold Price',
        'priceData'         : data
    }

    return render(request, 'production/goldPriceList.html', context)

@login_required
def add_gold_price(request):
    if request.method == 'POST':
        form = GoldPriceForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('price-list')
    else:
        form = GoldPriceForm()
    
    context = {
        'title'             : 'Gold Price Input',
        'head'              : 'Gold Price Input',
        'form'              : form
    }
    return render(request, 'production/addPrice.html', context)




@login_required
def add_costs(request):
    if request.method == 'POST':
        form = FinCostsForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('costs-list')
    else:
        form = FinCostsForm()
    
    context = {
        'title'             : 'Costs Data Input',
        'head'              : 'Costs Data Input',
        'form'              : form
    }
    return render(request, 'production/addCost.html', context)

@login_required
def tramming_list(request):

    data                   = trammings.objects.all().order_by('-date')
    context                = {
        'title'            : 'Tramming List',
        'head'             : 'Trammings',
        'trammingData'     :  data

    }

    return render (request, 'production/tramming.html', context)

@login_required
def add_trammings(request):
    if request.method == 'POST':
        form = TrammingForm(request.POST)
        if form.is_valid():
            form.save()
            message = ( f'New  record created succesfully.')
            messages.success(request,message)

            return redirect('tramming-list')
    else:
        form = TrammingForm()
    
    context = {
        'title'         : 'Input Tramming Data',
        'head'          : 'Enter Tramming Data',
        'form'          : form
    }
    return render(request, 'production/addTramming.html', context)

@login_required
def updateTrammingData(request, pk):
    data                            = get_object_or_404(trammings, id=pk)
    if request.method               == 'POST':
        form = TrammingForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()

            messages.success(request, f'Data has been updated successfully. ')
            return redirect('tramming-list')
    else:
        form = TrammingForm(instance=data)

    context = {
        'title'         : 'Update Tramming Data',
        'head'          : 'Update Tramming Data',
        'form'          : form,
        'data_id'       : pk
    }

    return render(request, 'production/updateTramming.html', context)