from django.urls import path, re_path
from .views import *
from production.views import *
from production.views import users_list
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # The home page
    path('', getData, name='dash'),
    path('dash', getData, name='dash'),
    path('costs', get_costs_dash, name='costs'),
    path('login/', login_view, name="login"),
    path('users', users_list, name='users-list'),
    path('create-user', create_user, name='create-user'),
    path('sperformance-list', safetyPrformance, name='sperformance-list'),
    path('add-sp', addSafetyPerfData, name='add-sp'), 
    path('update-sp/<int:pk>', updateSafetyData, name='update-sp'),   
    path('data-input', input_data, name='data-input'),
    path('update-data/<int:pk>', update_data, name='update-data'),
    path('scats-list', get_scats_tails, name='scats-list'),
    path('add-scats', addScatsTails, name='add-scats'),
    path('update-scats/<int:pk>', updateScatsTails, name='update-scats'),
    # path('production-input', enter_production_data, name='production-input'),
    path('targets', target_data_list, name='targets' ),
    path('input-targets', target_data, name='input-targets'),
    path('update-targets/<int:pk>', updateTargetData, name='update-targets'),
    path('budgets-list', budget_data_list, name='budgets-list'),
    path('add-budget', add_budget_data, name='add-budget'),
    path('summaries-list', summaries_list, name='summaries-list'),
    path('costs-summary', costs_details, name='costs-summary'),
    path('gold-summary', gold_estimate_details, name='gold-summary'),
    path('rom-summary', rom__details, name='rom-summary'),
    path('milling-summary', milling__details, name='milling-summary'),
    path('price-list', goldPriceList, name='price-list'),
    path('add-price', add_gold_price, name='add-price'),
    path('dept-spend-budget', get_dept_spend_budget, name='dept-spend-budget'),
    path('dept-spend-plan',get_dept_spend_plan, name='dept-spend-plan'),
    path('add-spending', add_dept_spending, name='add-spending'),
    path('add-spending-plan', add_dept_spending_plan, name='add-spending-plan'),
    path('add-spending-budget', add_dept_spending_budget, name='add-spending-budget'),
    path('spending-list', get_dept_spending, name='spending-list'),
    path('costs-list', cost_list, name='costs-list'),
    path('add-cost', add_costs, name='add-cost'),
    path('update-costs/<int:pk>', updateCost, name='update-costs'),
    path('cost-budget-list', cost_budgets_list, name='cost-budget-list'),
    path('add-cost-budget', add_cost_budget, name='add-cost-budget'),
    path('budgets-list', cost_budgets_list, name='budgets-list'),
    path('add-cost-budget', add_cost_budget, name='add-cost-budget'),
    path('tramming-details', ore_gen_details, name='tramming-details'),
    path('tramming-list', tramming_list, name='tramming-list'),
    path('add-tramming', add_trammings, name='add-tramming'),
    path('update-tramming/<int:pk>', updateTrammingData, name='update-tramming'),
    path("logout/", logout, name="logout")

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]