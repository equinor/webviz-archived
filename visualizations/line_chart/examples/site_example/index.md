{{ page_element('LineChart',
                './test.csv',
                check_box=true,
                xaxis='Time',
                yaxis='Value',
                logy=True,
                slider_columns=['dateslider'],
                dropdown_columns=['category'])
}}
