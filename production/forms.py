from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from app.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets                     = {
            'username'                  : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'email'                     : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'password1'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'password2'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
         }

        labels = {
            'username'                  : 'Username',
            'email'                     : 'Email',
            'password1'                 : 'Enter Password',
            'password2'                 : 'Re-type Password'
         }

class ProfileForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,  # Use predefined role choices
        widget=forms.Select(attrs={'class': 'form-control'}),  # Dropdown widget
        label='Role'
    )

    class Meta:
        model = Profile
        fields = ['role']


# class ProfileForm(forms.ModelForm):
#     role = forms.ModelChoiceField(
#         queryset=Profile.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         label='Role'
#     )

#     class Meta:
#         model = Profile
#         fields = ['role']
#         widgets                     = {
#             'role'                  : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
          
#          }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
class CostForm(forms.ModelForm):
    class Meta:
        model                       = Cost
        fields                      = ['date', 'c1', 'c2', 'c3', 'c1_cash_cost', 'c2_cash_cost', 'c3_cash_cost']
        widgets                     = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'c1'                    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'c2'                    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'c3'                    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'c1_cash_cost'          : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'c2_cash_cost'          : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'c3_cash_cost'          : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            
        }
        labels = {
            'date'                  : 'Date',
            'c1'                    : 'C1 Cost ($)',
            'c2'                    : 'C2 Cost ($)',
            'c3'                    : 'C3 Cost ($)',            
            'c1_cash_cost'          : 'C1 Cash Cost ($/oz)',
            'c2_cash_cost'          : 'C2 Cash Cost ($/oz)',
            'c3_cash_cost'          : 'C3 Cash Cost ($/oz)',
            'gold_price'            : 'Gold Price ($/oz)',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']



class EngineeringDataForm(forms.ModelForm):
    class Meta:
        model                       = Engineering_Data
        fields                      = ['date', 'zesa_downtime']

        widgets                     ={
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'zesa_downtime'         : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
        }
        labels                      = {
            'date'                  : 'Date',
            'zesa_downtime'         : 'Zesa Downtime (hrs)',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']       
        



class GoldPriceForm(forms.ModelForm):
    class Meta:
        model                       = GoldPrice
        fields                      = ['date', 'price']

        widgets                     = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'price'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),

        }
        labels                      = {
            'date'                  : 'Date',
            'price'                 : 'Gold Price ($/oz)',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']


class TrammingForm(forms.ModelForm):
    class Meta:
        model                       = trammings
        fields                      = ['date', 'western_top','western_top_grade', 'cymric_top','cymric_top_grade', 'cymric_bottom','cymric_bottom_grade', 'l_13','l_13_grade', 'l_15','l_15_grade', 'far_east','far_east_grade']

        widgets                     = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'western_top'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'western_top_grade'     : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'cymric_top'            : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'cymric_top_grade'      : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'cymric_bottom'         : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'cymric_bottom_grade'   : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'l_13'                  : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'l_13_grade'            : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'l_15'                  : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'l_15_grade'            : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'far_east'              : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'far_east_grade'        : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
        }

        labels = {
            'date'                  : 'Date',
            'western_top'           : 'Western Top Section (t)',
            'western_top_grade'     : 'Western Top Section Grade (g/t)',
            'cymric_top'            : 'Cymric Top Section (t)',
            'cymric_top_grade'      : 'Cymric Top Section Grade (g/t)',
            'cymric_bottom'         : 'Cymric Bottom Section (t)',   
            'cymric_bottom_grade'   : 'Cymric Bottom Section Grade (g/t)',
            'l_13'                  : '13 Level (t)',
            'l_13_grade'            : '13 Level Grade (g/t)',
            'l_15'                  : '15 Level (t)',
            'l_15_grade'            : '15 Level Grade (g/t)',
            'far_east'              : 'Far East (t)',
            'far_east_grade'        : 'Far East Grade (g/t)'
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']

# class DataForm(forms.ModelForm):
#     class Meta:
#         model                       = Data
#         fields                      = ['date', 'ug_tonnes', 'op_tonnes', 'milled_tonnes', 'dev_drilling', 'ore_gen', 'grade','cil_feed_grade', 'reconciled_grade', 'gold','recovery_perc', 'dowmtime', 'stock_pile']

#         widgets                     = {
#             'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
#             'ug_tonnes'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
#             'op_tonnes'             : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'milled_tonnes'         : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'dev_drilling'          : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'ore_gen'               : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'grade'                 : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'cil_feed_grade'        : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'reconciled_grade'      : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'gold'                  : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
#             'recovery_perc'         : forms.TextInput(attrs={'typr': 'text', 'class':'form-control'}),
#             'dowmtime'              : forms.TextInput(attrs={'type': 'text', 'placeholder':'Leave blank if None','class':'form-control'}),
#             'stock_pile'            : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),

#         }
#         labels = {
#             'date'                  : 'Date',
#             'ug_tonnes'             : 'Underground Trucked Tonnage (t)',
#             'op_tonnes'             : 'Open Pit Trucked Tonnage (t)',
#             'milled_tonnes'         : 'Milled Tonnes',            
#             'dev_drilling'          : 'Development Drilling (meters)',
#             'ore_gen'               : 'Ore Generation (t)',
#             'grade'                 : 'Trucked Grade (g/t)',
#             'cil_feed_grade'        : 'Carbon in Leach Grade (g/t)',
#             'reconciled_grade'      : 'Reconciled Grade (g/t)',
#             'gold'                  : 'Gold Produced (kg)',
#             'recovery_perc'         : 'Recovery (%)',
#             'dowmtime'              : 'Downtime (hrs)',
#             'stock_pile'            : 'Stock Pile (t)'
#         }

#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['date'].input_formats = ['%Y-%m-%d']

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['date', 'ug_tonnes', 'op_tonnes', 'milled_tonnes', 'dev_drilling', 'ore_gen', 
                  'grade', 'cil_feed_grade', 'reconciled_grade', 'gold', 'recovery_perc', 'stock_pile']

        widgets = {
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class': 'form-control'}),
            'ug_tonnes': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'op_tonnes': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'milled_tonnes': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'dev_drilling': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'ore_gen': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'cil_feed_grade': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'reconciled_grade': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'gold': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'recovery_perc': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            #'dowmtime': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Leave blank if None', 'class': 'form-control'}),
            'stock_pile': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }

        labels = {
            'date': 'Date',
            'ug_tonnes': 'Underground Trucked Tonnage (t)',
            'op_tonnes': 'Open Pit Trucked Tonnage (t)',
            'milled_tonnes': 'Milled Tonnes',
            'dev_drilling': 'Development Drilling (meters)',
            'ore_gen': 'Ore Generation (t)',
            'grade': 'Trucked Grade (g/t)',
            'cil_feed_grade': 'Carbon in Leach Grade (g/t)',
            'reconciled_grade': 'Reconciled Grade (g/t)',
            'gold': 'Gold Produced (kg)',
            'recovery_perc': 'Recovery (%)',
            #'dowmtime': 'Downtime (hrs)',
            'stock_pile': 'Stock Pile (t)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']
        # Make grade-related fields optional
        self.fields['grade'].required = False
        self.fields['cil_feed_grade'].required = False
        self.fields['reconciled_grade'].required = False
        self.fields['recovery_perc'].required = False
        #self.fields['dowmtime'].required=False
        self.fields['stock_pile'].required=False

class FinCostsForm(forms.ModelForm):
    class Meta:
        model = fin_costs
        fields = [
            'date', 'mining', 'mine_engineering', 'processing', 'hauling', 
            'tsd', 'owners', 'open_pit', 'depreciation', 'c3_cost', 
            'c1', 'c2', 'c3', 'gold_price'
        ]
        widgets = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'mining'                : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'mine_engineering'      : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'processing'            : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'hauling'               : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'tsd'                   : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'owners'                : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'open_pit'              : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'depreciation'          : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c3_cost'               : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c1'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c2'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c3'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'gold_price'            : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }
        labels = {
            'date'                  : 'Date',
            'mining'                : 'Mining Costs',
            'mine_engineering'      : 'Mine Engineering Costs',
            'processing'            : 'Processing Costs',
            'hauling'               : 'Hauling Costs',
            'tsd'                   : 'TSD Costs',
            'owners'                : 'Owners Costs',
            'open_pit'              : 'Open Pit Costs',
            'depreciation'          : 'Depreciation Costs',
            'c3_cost'               : 'C3 Cost',
            'c1'                    : 'C1 Cash Cost',
            'c2'                    : 'C2 Cash Cost',
            'c3'                    : 'C3 Cash Cost',
            'gold_price'            : 'Gold Price',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']


class FinCostsBudgetsForm(forms.ModelForm):
    class Meta:
        model = fin_cost_budgets
        fields = [
            'date', 'mining', 'mine_engineering', 'processing', 'hauling', 
            'tsd', 'owners', 'open_pit', 'depreciation', 'c3_cost', 
            'c1', 'c2', 'c3'
        ]
        widgets = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'mining'                : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'mine_engineering'      : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'processing'            : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'hauling'               : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'tsd'                   : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'owners'                : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'open_pit'              : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'depreciation'          : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c3_cost'               : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c1'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c2'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'c3'                    : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'gold_price'            : forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }
        labels = {
            'date'                  : 'Date',
            'mining'                : 'Mining Costs',
            'mine_engineering'      : 'Mine Engineering Costs',
            'processing'            : 'Processing Costs',
            'hauling'               : 'Hauling Costs',
            'tsd'                   : 'TSD Costs',
            'owners'                : 'Owners Costs',
            'open_pit'              : 'Open Pit Costs',
            'depreciation'          : 'Depreciation Costs',
            'c3_cost'               : 'C3 Cost',
            'c1'                    : 'C1 Cash Cost',
            'c2'                    : 'C2 Cash Cost',
            'c3'                    : 'C3 Cash Cost',
            'gold_price'            : 'Gold Price',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%Y-%m-%d']

class DeptSpendingPlanForm(forms.ModelForm):

    department = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Department'
    )
    class Meta:
        model                     = dept_spending_plan
        fields                     = ['date', 'labour', 'utilities', 'stores', 'repairs', 'hauling', 'loading', 'processing', 'open_pit', 'social_ammenities', 'security', 'other_overheads', 'imtt', 'department']
        widgets                    = {
            'date'                 : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'labour'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'utilities'            : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'stores'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'repairs'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'hauling'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'loading'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'processing'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'open_pit'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'social_ammenities'    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'security'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'other_overheads'      : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'imtt'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'department'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),

        }
        labels = {
            'date'                  : 'Date',
            'labour'                : 'Labour ($)',
            'utilities'             : 'Utilities ($)',
            'stores'                : 'Stores ($)',
            'repairs'               : 'Repairs ($)',
            'hauling'               : 'Hauling ($)',
            'processing'            : 'Processing ($)',
            'open_pit'              : 'Open Pit ($)',
            'social_ammenities'     : 'Social Ammenities ($)',
            'security'              : 'Security ($)',
            'other_overheads'       : 'Other Overheads ($)',
            'imtt'                  : 'IMTT ($)',
            'department'            : 'Department'
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']

class DeptSpendingBudgetForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Department'
    )


    class Meta:
        model                      = fin_budgets
        fields                     = ['date', 'labour', 'utilities', 'stores', 'repairs', 'hauling', 'loading', 'processing', 'open_pit', 'social_ammenities', 'security', 'other_overheads', 'imtt', 'department']
        widgets                    = {
            'date'                 : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'labour'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'utilities'            : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'stores'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'repairs'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'hauling'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'loading'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'processing'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'open_pit'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'social_ammenities'    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'security'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'other_overheads'      : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'imtt'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'department'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),

        }
        labels = {
            'date'                  : 'Date',
            'labour'                : 'Labour ($)',
            'utilities'             : 'Utilities ($)',
            'stores'                : 'Stores ($)',
            'repairs'               : 'Repairs ($)',
            'hauling'               : 'Hauling ($)',
            'processing'            : 'Processing ($)',
            'open_pit'              : 'Open Pit ($)',
            'social_ammenities'     : 'Social Ammenities ($)',
            'security'              : 'Security ($)',
            'other_overheads'       : 'Other Overheads ($)',
            'imtt'                  : 'IMTT ($)',
            'department'            : 'Department'
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']

class DeptSpendingForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Department'
    )


    class Meta:
        model                      = dept_spending
        fields                     = ['date', 'labour', 'utilities', 'stores', 'repairs', 'hauling', 'loading', 'processing', 'open_pit', 'social_ammenities', 'security', 'other_overheads', 'imtt', 'department']
        widgets                    = {
            'date'                 : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'labour'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'utilities'            : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'stores'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'repairs'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'hauling'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'loading'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'processing'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'open_pit'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'social_ammenities'    : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'security'             : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'other_overheads'      : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'imtt'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'department'           : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),

        }
        labels = {
            'date'                  : 'Date',
            'labour'                : 'Labour ($)',
            'utilities'             : 'Utilities ($)',
            'stores'                : 'Stores ($)',
            'repairs'               : 'Repairs ($)',
            'hauling'               : 'Hauling ($)',
            'processing'            : 'Processing ($)',
            'open_pit'              : 'Open Pit ($)',
            'social_ammenities'     : 'Social Ammenities ($)',
            'security'              : 'Security ($)',
            'other_overheads'       : 'Other Overheads ($)',
            'imtt'                  : 'IMTT ($)',
            'department'            : 'Department'
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']

class SafertyPerformanceForm(forms.ModelForm):
    class Meta:
        model                       = SafetyPerformance
        fields                      = ['date', 'fatality', 'lti', 'nlti']
        widgets                     = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'fatality'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'lti'                   : forms.TextInput(attrs={'type': 'text', 'class':'form-control', }),
            'nlti'                  : forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
        }
        labels = {
            'date'                  : 'Date',
            'fatality'              : 'Fatality',
            'lti'                   : 'Lost Time Incident',
            'nlti'                  : 'Non-Lost Time Incident',
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']


class PlanForm(forms.ModelForm):
    class Meta:
        model                       = plan
        fields                      = [ 'date', 'rom', 'milled_tonnes', 'gold', 'grade', 'dev_drilling', 'ore_gen','recovery']
        widgets                     = {

           'date'                   : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'rom'                   : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'milled_tonnes'         : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'gold'                  : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'grade'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'dev_drilling'          : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'ore_gen'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'recovery'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            }
        labels = {
            'date'                  : 'Date',
            'rom'                   : 'R.O.M (tonnes)',
            'milled_tonnes'         : 'Milled Tonnes (tonnes)',
            'gold'                  : 'Gold (kg)',
            'grade'                 : 'Grade (kg/tonnes)',
            'dev_drilling'          : 'Development Drilling (meters)',
            'ore_gen'               : 'Ore Generation (tonnes)',
            'recovery'              : 'Recovery %'
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']


class BudgetsForm(forms.ModelForm):
    class Meta:
        model                       = budget
        fields                      = [ 'date', 'rom', 'milled_tonnes', 'gold', 'grade', 'dev_drilling', 'ore_gen', 'recovery']
        widgets                     = {

           'date'                   : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'rom'                   : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'milled_tonnes'         : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'gold'                  : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'grade'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'dev_drilling'          : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'ore_gen'               : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'recovery'              : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
        }
        labels = {
            'date'                  : 'Date',
            'rom'                   : 'R.O.M (tonnes)',
            'milled_tonnes'         : 'Milled Tonnes (tonnes)',
            'gold'                  : 'Gold (kg)',
            'grade'                 : 'Grade (kg/tonnes)',
            'dev_drilling'          : 'Development Drilling (meters)',
            'ore_gen'               : 'Ore Generation (tonnes)',
             'recovery'              : 'Recovery %'
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']


class GoldEstimateForm(forms.ModelForm):
    class Meta:
        model                       = gold_estimate
        fields                      = ['date', 'cil', 'scats', 'grg']
        widgets                     = {
            'date'                  : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date',  'class':'form-control'}),
            'cil'                   : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'scats'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'grg'                   : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            # 'total'                 : forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
        }
        labels = {
            'date'                  : 'Date',
            'cil'                   : 'CIL ',
            'scats'                 : 'SCATS',
            'grg'                   : 'GRG',
            # 'total'                 : 'TOTAL',
            
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date'].input_formats = ['%Y-%m-%d']