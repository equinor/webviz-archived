{{ page_element(
    'LineChart',
    './test.csv',
    logy=True,
    xaxis='Time',
    yaxis='Value',
    slider_columns=['dateslider'],
    dropdown_columns=['category'])
}}
