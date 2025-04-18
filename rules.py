from skfuzzy import control as ctrl

def create_rules(variables):
    demand = variables['demand']
    availability = variables['availability']
    urgency = variables['urgency']
    proximity = variables['proximity']
    weather = variables['weather']
    time_of_day = variables['time_of_day']
    day_of_week = variables['day_of_week']
    season = variables['season']
    price_adjustment = variables['price_adjustment']
    
    rule1 = ctrl.Rule(demand['high'] & availability['scarce'] & urgency['high'], price_adjustment['increase'])
    rule2 = ctrl.Rule(demand['low'] & availability['plentiful'], price_adjustment['decrease'])
    rule3 = ctrl.Rule(demand['moderate'] & urgency['low'], price_adjustment['maintain'])
    rule4 = ctrl.Rule(demand['high'] & availability['moderate'], price_adjustment['increase'])
    rule5 = ctrl.Rule(demand['low'] & urgency['low'], price_adjustment['decrease'])
    rule6 = ctrl.Rule(demand['moderate'] & availability['plentiful'], price_adjustment['maintain'])
    rule7 = ctrl.Rule(availability['scarce'] & urgency['high'], price_adjustment['increase'])
    rule8 = ctrl.Rule(demand['high'] & availability['plentiful'] & urgency['low'], price_adjustment['maintain'])

    rule9 = ctrl.Rule(proximity['far'] & weather['poor'], price_adjustment['increase'])
    rule10 = ctrl.Rule(proximity['near'] & weather['good'], price_adjustment['decrease'])
    rule11 = ctrl.Rule(proximity['far'] & urgency['high'], price_adjustment['increase'])
    rule12 = ctrl.Rule(weather['poor'] & availability['scarce'], price_adjustment['increase'])
    rule13 = ctrl.Rule(weather['good'] & availability['plentiful'], price_adjustment['decrease'])
    rule14 = ctrl.Rule(proximity['near'] & weather['poor'] & urgency['high'], price_adjustment['increase'])
    rule15 = ctrl.Rule(proximity['far'] & weather['good'] & availability['plentiful'], price_adjustment['maintain'])
    rule16 = ctrl.Rule(proximity['medium'] & weather['fair'] & demand['moderate'], price_adjustment['maintain'])

    rule17 = ctrl.Rule(time_of_day['night'], price_adjustment['increase'])
    rule18 = ctrl.Rule(time_of_day['business_hours'] & availability['plentiful'], price_adjustment['decrease'])
    rule19 = ctrl.Rule(time_of_day['evening'] & demand['high'], price_adjustment['increase'])
    rule20 = ctrl.Rule(time_of_day['early_morning'] & demand['low'], price_adjustment['decrease'])

    rule21 = ctrl.Rule(day_of_week['weekend'] & demand['high'], price_adjustment['increase'])
    rule22 = ctrl.Rule(day_of_week['weekday'] & time_of_day['business_hours'] & demand['low'], price_adjustment['decrease'])
    rule23 = ctrl.Rule(day_of_week['weekend'] & availability['scarce'], price_adjustment['increase'])
    rule24 = ctrl.Rule(day_of_week['weekday'] & availability['plentiful'], price_adjustment['decrease'])

    rule25 = ctrl.Rule(season['winter'] & weather['poor'], price_adjustment['increase'])
    rule26 = ctrl.Rule(season['summer'] & weather['good'], price_adjustment['decrease'])
    rule27 = ctrl.Rule(season['winter'] & proximity['far'], price_adjustment['increase'])
    rule28 = ctrl.Rule(season['spring'] & demand['moderate'], price_adjustment['maintain'])

    rule29 = ctrl.Rule(time_of_day['night'] & weather['poor'] & proximity['far'], price_adjustment['increase'])
    rule30 = ctrl.Rule(day_of_week['weekend'] & season['summer'] & weather['good'], price_adjustment['increase'])
    rule31 = ctrl.Rule(day_of_week['weekday'] & time_of_day['business_hours'] & weather['good'], price_adjustment['decrease'])
    rule32 = ctrl.Rule(season['winter'] & day_of_week['weekend'] & demand['high'], price_adjustment['increase'])

    rules = [
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
        rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16,
        rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24,
        rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32
    ]
    
    return rules