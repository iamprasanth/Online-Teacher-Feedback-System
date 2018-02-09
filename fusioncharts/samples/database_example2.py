from django.shortcuts import render
from django.http import HttpResponse
from multilingual_survey .models import Answer

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from ..fusioncharts import FusionCharts

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered.

def chart(request):
	# Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
	dataSource = {}
	dataSource['chart'] = { 
		"caption" : "How Fast are the classes being taken?",
        #"subCaption" : "Last year",
        "paletteColors" : "#0075c2,#1aaf5d,#f2c500,#f45b00,#8e0000",
        "bgColor" : "#ffffff",
        "showBorder" : "0",
        "use3DLighting" : "0",
        "showShadow" : "0",
        "enableSmartLabels" : "0",
        "startingAngle" : "0",
        "showPercentValues" : "1",
        "showPercentInTooltip" : "0",
        "decimals" : "1",
        "captionFontSize" : "14",
        "subcaptionFontSize" : "14",
        "subcaptionFontBold" : "0",
        "toolTipColor" : "#ffffff",
        "toolTipBorderThickness" : "0",
        "toolTipBgColor" : "#000000",
        "toolTipBgAlpha" : "80",
        "toolTipBorderRadius" : "2",
        "toolTipPadding" : "5",
        "showHoverEffect" : "1",
        "showLegend" : "1",
        "legendBgColor" : "#ffffff",
        "legendBorderAlpha" : "0",
        "legendShadow" : "0",
        "legendItemFontSize" : "10",
        "legendItemFontColor" : "#666666",
        "useDataPlotColorForLabels" : "1"
		}

	# Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	dataSource['data'] = [] 
    # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
	count = 0
	
	counter = 0

	countest = 0
	
	for key in Answer.objects.all():

		if key.choice_id == 19 :
			count +=1
		elif key.choice_id == 20 :
			counter +=1
		elif key.choice_id == 21 :
			countest +=1
	data = {}
	data['label'] = "Very "
	data['value'] = count
	dataSource['data'].append(data)
	data = {}
	data['label'] = "Not much so"
	data['value'] = counter
	dataSource['data'].append(data)
	data = {}
	data['label'] = "Not at all"
	data['value'] = countest
	dataSource['data'].append(data)

    # Create an object for the Pie 2D chart using the FusionCharts class constructor        	  		
	pie2D = FusionCharts("pie2D", "ex1" , "600", "400", "chart-1", "json", dataSource)
	return render(request, 'index1.html', {'output': pie2D.render()}) 
