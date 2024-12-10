def empInfo(name, /, age, *,dept):
    print(name, age, dept)
empInfo('Pranab', age=40, dept='HRD')
empInfo(('Pranab',40, 'HRD'))
empInfo(name='Pranab', age=40, dept='HRD')