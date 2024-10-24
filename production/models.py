from django.db import models
from django.db.models import Sum
from django.utils.functional import cached_property

# Create your models here.
class Data(models.Model):
    date                        = models.DateField(unique=True)
    ug_tonnes                   = models.FloatField()
    op_tonnes                   = models.FloatField()
    milled_tonnes               = models.FloatField()
    dev_drilling                = models.FloatField()
    ore_gen                     = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cil_feed_grade              = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reconciled_grade            = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True)
    gold                        = models.DecimalField(max_digits=10, decimal_places=4)
    recovery_perc               = models.DecimalField(max_digits=10, decimal_places=2)
    dowmtime                    = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_pile                  = models.FloatField()

    def __str__(self) -> str:
        return f'{self.ug_tonnes + self.op_tonnes}'

    # @cached_property
    # def stock_pile(self):
        
    #     # Calculate the YTD trucking and milling
    #     ytd_trucking = Data.objects.filter(date__lte=self.date).aggregate(
    #         ytd_trucking=Sum('ug_tonnes') + Sum('op_tonnes')
    #     )['ytd_trucking']
    #     ytd_milling = Data.objects.filter(date__lte=self.date).aggregate(
    #         ytd_milling=Sum('milled_tonnes')
    #     )['ytd_milling']

    #     #previous_stock_pile = ytd_trucking - ytd_milling if ytd_trucking and ytd_milling else 0
    #     previous_stock_pile = 2555
    #     # Calculate current day's stockpile
    #     current_day_stock = self.ug_tonnes + self.op_tonnes - self.milled_tonnes

    #     return previous_stock_pile + current_day_stock

class Engineering_Data(models.Model):
    date                        = models.DateField(unique=True)
    zesa_downtime               = models.FloatField()


    def __str__(self) -> str:
        return f'{self.zesa_downtime} on {self.date}'


class SafetyPerformance(models.Model):
    date                        = models.DateField(unique =True)
    fatality                    = models.IntegerField()
    lti                         = models.IntegerField()
    nlti                        = models.IntegerField()
    #add lost time variable

    def __str__(self) -> str:
        return f'{self.fatality} fatalities on {self.date}'

class FatalityFreeShifts(models.Model):
    date                        = models.DateField(unique=True)
    shifts                      = models.IntegerField()

    def __str__(self):
        return f'{self.shifts} - {self.date.month}'
    
class plan(models.Model):
    date                        = models.DateField(unique=True)
    rom                         = models.FloatField()
    milled_tonnes               = models.FloatField()
    gold                        = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2)
    dev_drilling                = models.FloatField()
    ore_gen                     = models.FloatField()
    recovery                    = models.DecimalField(max_digits=5, decimal_places=2)

    def values(self):
        return {
            'date'              : self.date,
            'rom'               : self.rom,
            'milled_tonnes'     : self.milled_tonnes,
            'gold'              : self.gold,
            'grade'             : self.grade,
            'dev_drilling'      : self.dev_drilling,
            'ore_gen'           : self.ore_gen,
            'recovery'          : self.recovery

        }
class budget(models.Model):
    date                        = models.DateField(unique=True)
    rom                         = models.FloatField()
    milled_tonnes               = models.FloatField()
    gold                        = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2)
    dev_drilling                = models.FloatField()
    ore_gen                     = models.FloatField()
    recovery                    = models.DecimalField(max_digits=5, decimal_places=2)

    def values(self):
        return {
            'date'              : self.date,
            'rom'               : self.rom,
            'milled_tonnes'     : self.milled_tonnes,
            'gold'              : self.gold,
            'grade'             : self.grade,
            'dev_drilling'      : self.dev_drilling,
            'ore_gen'           : self.ore_gen,
            'recovery'          : self.recovery
        }
class prod_budget(models.Model):
    date                        = models.DateField(unique=True)
    rom                         = models.FloatField()
    milled_tonnes               = models.FloatField()
    gold                        = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2)
    dev_drilling                = models.FloatField()
    ore_gen                     = models.FloatField()
    recovery                    = models.DecimalField(max_digits=5, decimal_places=2)

    def values(self):
        return {
            'date'              : self.date,
            'rom'               : self.rom,
            'milled_tonnes'     : self.milled_tonnes,
            'gold'              : self.gold,
            'grade'             : self.grade,
            'dev_drilling'      : self.dev_drilling,
            'ore_gen'           : self.ore_gen,
            'recovery'          : self.recovery
        }



class Summaries(models.Model):
    date                        = models.DateField()
    tonnes_trucked              = models.FloatField()
    tonnes_hoisted              = models.FloatField()
    # tonnes_trammed              = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2) #should be changed to gold ounces
    meters_drilled              = models.DecimalField(max_digits=10, decimal_places=2)
    tonnes_blasted              = models.FloatField()
    downtime                    = models.DecimalField(max_digits=10, decimal_places=2)
    gold                        = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.tonnes_trucked} tonnes trucked on {self.date}'
    
class budgets(models.Model):
    month                       = models.DateField()
    trucked                     = models.FloatField()
    hoisted                     = models.FloatField()
    gold                        = models.FloatField()
    grade                       = models.DecimalField(max_digits=10, decimal_places=2)
    drilling                    = models.FloatField()
    blasting                    = models.FloatField()

    def values(self):
        return {
            'month'             : self.month,
            'trucked'           : self.trucked,
            'hoisted'           : self.hoisted,
            'gold'              : self.gold,
            'grade'             : self.grade,
            'drilling'          : self.drilling,
            'blasting'          : self.blasting
        }
    # def __str__(self)-> str:
    #     return f'{self.grade} targeted for the month of {self.month}'


class Production_Data(models.Model):
    date                        = models.DateField(unique=True)
    trucked_tonnage             = models.FloatField()
    open_pit_tonnage            = models.FloatField()
    cymric_tonnage              = models.FloatField()
    cymric_day                  = models.FloatField()
    cymric_night                = models.FloatField()
    bottom_section_total        = models.FloatField()
    milled_tonnage              = models.FloatField()

class cash_costs(models.Model):
    date                        = models.DateField(unique=True)     
    c1                          = models.DecimalField(max_digits=10, decimal_places =2)
    c2                          = models.DecimalField(max_digits=10, decimal_places =2)         
    c3                          = models.DecimalField(max_digits=10, decimal_places =2)
    gold_price                  = models.DecimalField(max_digits=10, decimal_places =2)
    

class fin_costs(models.Model):
    date                        = models.DateField(unique=True)
    mining                      = models.DecimalField(max_digits=10, decimal_places=2)
    mine_engineering            = models.DecimalField(max_digits=10, decimal_places=2)
    processing                  = models.DecimalField(max_digits=10, decimal_places=2)
    hauling                     = models.DecimalField(max_digits=10, decimal_places=2)
    tsd                         = models.DecimalField(max_digits=10, decimal_places=2)
    owners                      = models.DecimalField(max_digits=10, decimal_places=2)
    open_pit                    = models.DecimalField(max_digits=10, decimal_places=2)

    depreciation                = models.DecimalField(max_digits=10, decimal_places=2)
    c3_cost                     = models.DecimalField(max_digits=10, decimal_places=2)

    c1                          = models.DecimalField(max_digits=10, decimal_places=2)
    c2                          = models.DecimalField(max_digits=10, decimal_places=2)
    c3                          = models.DecimalField(max_digits=10, decimal_places=2)

    gold_price                  = models.DecimalField(max_digits=10, decimal_places=2)


    @cached_property
    def total_c1_cost(self):
        return (self.mining + self.mine_engineering + self.processing +
                self.hauling + self.tsd + self.owners + self.open_pit)

    @cached_property
    def total_c2_cost(self):
        return self.total_c1_cost + self.depreciation

    @cached_property
    def total_c3_cost(self):
        return self.total_c2_cost + self.c3_cost

    def __str__(self):
        return f'Costs for {self.date}'


class fin_cost_budgets(models.Model):
    date                        = models.DateField(unique=True)
    mining                      = models.DecimalField(max_digits=10, decimal_places=2)
    mine_engineering            = models.DecimalField(max_digits=10, decimal_places=2)
    processing                  = models.DecimalField(max_digits=10, decimal_places=2)
    hauling                     = models.DecimalField(max_digits=10, decimal_places=2)
    tsd                         = models.DecimalField(max_digits=10, decimal_places=2)
    owners                      = models.DecimalField(max_digits=10, decimal_places=2)
    open_pit                    = models.DecimalField(max_digits=10, decimal_places=2)

    depreciation                = models.DecimalField(max_digits=10, decimal_places=2)
    c3_cost                     = models.DecimalField(max_digits=10, decimal_places=2)

    c1                          = models.DecimalField(max_digits=10, decimal_places=2)
    c2                          = models.DecimalField(max_digits=10, decimal_places=2)
    c3                          = models.DecimalField(max_digits=10, decimal_places=2)

    @cached_property
    def total_c1_cost_budget(self):
        return (self.mining + self.mine_engineering + self.processing +
                self.hauling + self.tsd + self.owners + self.open_pit)

    @cached_property
    def total_c2_cost_budget(self):
        return self.total_c1_cost_budget + self.depreciation

    @cached_property
    def total_c3_cost_budget(self):
        return self.total_c2_cost_budget + self.c3_cost

    def __str__(self):
        return f'Budgets for {self.date}'

class Departments(models.Model):
    name                        = models.CharField(max_length=100)
    description                 = models.TextField()
    head                        = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Costs_centers(models.Model):
    center_id                   = models.CharField(max_length=20)
    department                  = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='dept_cost_center')
    

class sections(models.Model):
    section                     = models.CharField(max_length=100)
    description                 = models.TextField()

class fin_budgets(models.Model):
    date                        = models.DateField()
    labour                      = models.DecimalField(max_digits=10, decimal_places=2)
    utilities                   = models.DecimalField(max_digits=10, decimal_places=2)
    stores                      = models.DecimalField(max_digits=10, decimal_places=2)
    repairs                     = models.DecimalField(max_digits=10, decimal_places=2)
    hauling                     = models.DecimalField(max_digits=10, decimal_places=2)
    loading                     = models.DecimalField(max_digits=10, decimal_places=2)
    processing                  = models.DecimalField(max_digits=10, decimal_places=2)
    open_pit                    = models.DecimalField(max_digits=10, decimal_places=2)
    social_ammenities           = models.DecimalField(max_digits=10, decimal_places=2)
    security                    = models.DecimalField(max_digits=10, decimal_places=2)
    other_overheads             = models.DecimalField(max_digits=10, decimal_places=2)
    imtt                        = models.DecimalField(max_digits=10, decimal_places=2)
    department                  = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='dept_cost')

    @cached_property
    def total_c1_cost(self):
        return (self.labour + self.utilities + self.processing + self.stores + self.other_overheads +
                self.hauling + self.loading + self.repairs + self.open_pit + self.imtt + self.security + self.repairs)
    


class dept_spending_plan(models.Model):
    date                        = models.DateField()
    labour                      = models.DecimalField(max_digits=10, decimal_places=2)
    utilities                   = models.DecimalField(max_digits=10, decimal_places=2)
    stores                      = models.DecimalField(max_digits=10, decimal_places=2)
    repairs                     = models.DecimalField(max_digits=10, decimal_places=2)
    hauling                     = models.DecimalField(max_digits=10, decimal_places=2)
    loading                     = models.DecimalField(max_digits=10, decimal_places=2)
    processing                  = models.DecimalField(max_digits=10, decimal_places=2)
    open_pit                    = models.DecimalField(max_digits=10, decimal_places=2)
    social_ammenities           = models.DecimalField(max_digits=10, decimal_places=2)
    security                    = models.DecimalField(max_digits=10, decimal_places=2)
    other_overheads             = models.DecimalField(max_digits=10, decimal_places=2)
    imtt                        = models.DecimalField(max_digits=10, decimal_places=2)
    department                  = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='dept_plan')

    @cached_property
    def total_c1_cost(self):
        return (self.labour + self.utilities + self.processing + self.stores + self.other_overheads +
                self.hauling + self.loading + self.repairs + self.open_pit + self.imtt + self.security + self.repairs)
    

   
    
class dept_spending(models.Model):
    date                        = models.DateField()
    labour                      = models.DecimalField(max_digits=10, decimal_places=2)
    utilities                   = models.DecimalField(max_digits=10, decimal_places=2)
    stores                      = models.DecimalField(max_digits=10, decimal_places=2)
    repairs                     = models.DecimalField(max_digits=10, decimal_places=2)
    hauling                     = models.DecimalField(max_digits=10, decimal_places=2)
    loading                     = models.DecimalField(max_digits=10, decimal_places=2)
    processing                  = models.DecimalField(max_digits=10, decimal_places=2)
    open_pit                    = models.DecimalField(max_digits=10, decimal_places=2)
    social_ammenities           = models.DecimalField(max_digits=10, decimal_places=2)
    security                    = models.DecimalField(max_digits=10, decimal_places=2)
    other_overheads             = models.DecimalField(max_digits=10, decimal_places=2)
    imtt                        = models.DecimalField(max_digits=10, decimal_places=2)
    department                  = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='dept_spend')



    @cached_property
    def total_c1_cost(self):
        return (self.labour + self.utilities + self.processing + self.stores + self.other_overheads +
                self.hauling + self.loading + self.repairs + self.open_pit + self.imtt + self.security + self.repairs)
    



class Costs(models.Model):
    date                        = models.DateField(unique=True)
    c1                          = models.DecimalField(max_digits=10, decimal_places=2)
    c2                          = models.DecimalField(max_digits=10, decimal_places=2)
    c3                          = models.DecimalField(max_digits=10, decimal_places=2)

    c1_cash_cost                = models.DecimalField(max_digits=10, decimal_places=2)
    c2_cash_cost                = models.DecimalField(max_digits=10, decimal_places=2)
    c3_cash_cost                = models.DecimalField(max_digits=10, decimal_places=2)

    gold_price                  = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.c1}'


class Cost(models.Model):
    date                    = models.DateField(unique=True)
    c1                      = models.DecimalField(max_digits=10, decimal_places=2)
    c2                      = models.DecimalField(max_digits=10, decimal_places=2)
    c3                      = models.DecimalField(max_digits=10, decimal_places=2)

    c1_cash_cost            = models.DecimalField(max_digits=10, decimal_places=2)
    c2_cash_cost            = models.DecimalField(max_digits=10, decimal_places=2)
    c3_cash_cost            = models.DecimalField(max_digits=10, decimal_places=2)

    gold_price              = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.c1}'
class GoldPrice(models.Model):
    date                    = models.DateField(unique=True)
    price                   = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.price} on {self.date}'
    

class trammings(models.Model):
    date                    = models.DateField(unique=True)
    western_top             = models.FloatField()
    western_top_grade       = models.DecimalField(max_digits=10, decimal_places=2)          # New field for grade
    cymric_top              = models.FloatField()
    cymric_top_grade        = models.DecimalField(max_digits=10, decimal_places=2)           # New field for grade
    cymric_bottom           = models.FloatField()
    cymric_bottom_grade     = models.DecimalField(max_digits=10, decimal_places=2)           # New field for grade
    l_13                    = models.FloatField()
    l_13_grade              = models.DecimalField(max_digits=10, decimal_places=2)           # New field for grade
    l_15                    = models.FloatField()
    l_15_grade              = models.DecimalField(max_digits=10, decimal_places=2)           # New field for grade
    far_east                = models.FloatField()
    far_east_grade          = models.DecimalField(max_digits=10, decimal_places=2)           # New field for grade

    def __str__(self):
        total_tonnage = self.western_top + self.cymric_top + self.cymric_bottom + self.l_13 + self.l_15 + self.far_east
        return f'Total Tonnage = {total_tonnage}'



class prod_downtime(models.Model):
    section                     = models.ForeignKey(sections, on_delete=models.CASCADE, related_name='mine_section')
    date                        = models.DateField()
    downtime                    = models.DecimalField(max_digits=10, decimal_places=2)
    reason                      = models.TextField()


class gold_estimate(models.Model):
    date                        = models.DateField(unique=True)
    cil                         = models.DecimalField(max_digits=10, decimal_places=4)
    scats                       = models.DecimalField(max_digits=10, decimal_places=4)
    grg                         = models.DecimalField(max_digits=10, decimal_places=5)
   

    def __str__(self):
        return f'{self.date} = {self.total} gold'
    
    @cached_property
    def total(self):
        return (self.cil + self.scats + self.grg)
    