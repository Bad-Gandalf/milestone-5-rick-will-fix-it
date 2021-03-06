   const OpenFeaturesContributionsApi = function() {
    this.init = function() {
    queue()
        .defer(d3.json, "/stats/api/chart/data/feature/open/contributions")
        .await(makeGraphs);
    };
    function makeGraphs(error, data) {
    data.forEach(function(d) {
        d.title = d.title;
        d.price = +d.price;
        d.contributions = +d3.sum(d.contributions);
        d.author = d.author;});
            
        console.log(data);
        show_open_features_contributions(data);
        dc.renderAll();
    }
    

    function show_open_features_contributions(data) {
       
        var margin = {top: 25, right: 40, bottom: 35, left: 85},
				w = 1000 - margin.left - margin.right,
				h = 350 - margin.top - margin.bottom;
       
		// Not perfect but in order for the correct legends additional blank colours added.
		// Could not find a work around.
        var colors =	{0:	["Price", "#377EB8"],
				     1:	["Contributions", "#4DAF4A"],
                     2: [" ", "#ffffff"],
                     3: [" ", "#ffffff"],
                     4: [" ", "#ffffff"],
                     5: [" ", "#ffffff"],
                     6: [" ", "#ffffff"],
                     7: [" ", "#ffffff"],
                     8: [" ", "#ffffff"],
                     9: [" ", "#ffffff"],
                     10: [" ", "#ffffff"],
       };

		var titles = [];
		for (var i = 0; i < data.length; i++){
		    titles.push(data[i].title);
		}
						    

		var xScale = d3.scale.ordinal()
						.domain(d3.range(data.length))
						.rangeRoundBands([0, w-40], 0.05); 
		// ternary operator to determine if global or local has a larger scale
		var yScale = d3.scale.linear()
						.domain([0, d3.max(data, function(d) { return (d.price > d.contributions) ? d.price : d.contributions;})]) 
						.range([h, 0]);
						
		var xAxis = d3.svg.axis()
						.scale(xScale)
						.orient("bottom")
						.ticks(data.length)
						.tickFormat(function(d, i) { return titles[i]; });
						
		var yAxis = d3.svg.axis()
						.scale(yScale)
						.orient("left")
						.ticks(10);
				
		
	
		var commaFormat = d3.format(',');
		
		//SVG element
		var svg = d3.select("#open-features_contributions")
					.append("svg")
					.attr("width", w + margin.left + margin.right)
					.attr("height", h + margin.top + margin.bottom)
					.append("g")
					.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
			
		// Graph Bars
		var sets = svg.selectAll(".set") 
			.data(data) 
			.enter()
			.append("g")
		    .attr("class","set")
		    .attr("transform",function(d,i){
		         return "translate(" + xScale(i) + ",0)";
		     })
			;
		
		sets.append("rect")
		    .attr("class","price")
			.attr("width", xScale.rangeBand()/2)
			.attr("y", function(d) {
				return yScale(d.price);
			})
		    .attr("x", xScale.rangeBand()/2)
		    .attr("height", function(d){
		        return h - yScale(d.price);
		    })
			.attr("fill", colors[0][1])
			.append("text")
		   .text(function(d) {
				return commaFormat(d.price);
		   })
		   .attr("text-anchor", "middle")
		   .attr("x", function(d, i) {
				return xScale(i) + xScale.rangeBand() / 2;
		   })
		   .attr("y", function(d) {
				return h - yScale(d.price) + 14;
		   })
		   .attr("font-family", "sans-serif") 
		   .attr("font-size", "11px")
		   .attr("fill", "black")
		   	;
		
		sets.append("rect")
		    .attr("class","contributions")
			.attr("width", xScale.rangeBand()/2)
			.attr("y", function(d) {
				return yScale(d.contributions);
			})
		    .attr("height", function(d){
		        return h - yScale(d.contributions);
		    })
			.attr("fill", colors[1][1])
			.append("text")
			.text(function(d) {
				return commaFormat(d.contributions);
			})
			.attr("text-anchor", "middle")
			.attr("x", function(d,i){return (w +(140*i));})
			.attr("y", function(d) {
				return h - yScale(d.contributions) + 14;
			})
			.attr("font-family", "sans-serif") 
			.attr("font-size", "11px")
			.attr("fill", "red")
			;
		   
		// xAxis
		svg.append("g") // Add the X Axis
			.attr("class", "x axis")
			.attr("transform", "translate(0," + (h) + ")")
			.call(xAxis)
				;
		// yAxis
		svg.append("g")
			.attr("class", "y axis")
			.attr("transform", "translate(0 ,0)")
			.call(yAxis)
			;
		// xAxis label
		svg.append("text") 
			.attr("transform", "translate(" + (w / 2) + " ," + (h + margin.bottom - 2) +")")
			.style("text-anchor", "middle")
			.text("Features");
		//yAxis label
		svg.append("text")
				
				.attr("y", 95)
				.attr("x", -70)
				.attr("dy", "1em")
				.attr("font-family", "sans-serif") 
		        .attr("font-size", "30px")
				.style("text-anchor", "middle")
				.text("€");
		
		
		
		
		// add legend   
		var legend = svg.append("g")
				.attr("class", "legend")
				//.attr("x", w - 65)
				//.attr("y", 50)
				.attr("height", 100)
				.attr("width", 100)
				.attr('transform', 'translate(20,50)');
		
		
		legend.selectAll('rect')
				.data(data)
				.enter()
				.append("rect")
				.attr("x", w - 65)
				.attr("y", function(d, i) {
					return i * 20;
				})
				.attr("width", 10)
				.attr("height", 10)
				
				.style("fill", function(d) {
					var color = colors[data.indexOf(d)][1];
					return color;
				});
		
		legend.selectAll('text')
				.data(data)
				.enter()
				.append("text")
				.attr("x", w - 52)
				.text(function(d) {
					var text = colors[data.indexOf(d)][0];
					return text;})
				.attr("y", function(d, i) {
					return i * 20 + 9;
				
				});
		
	
    }
};

const T = new OpenFeaturesContributionsApi();

T.init();