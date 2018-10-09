     const BugUpvotesApi = function() {
        this.init = function() {
            queue()
                .defer(d3.json, "/stats/api/chart/data/bug/working/upvotes")
                .await(makeGraphs);
        };

        function makeGraphs(error, data) {
            data.forEach(function(d) {
                d.title = d.title;
                d.total_upvotes = +d.total_upvotes;
            });

            console.log(data);
            show_working_bug_upvotes(data);
            dc.renderAll();
        }

        function show_working_bug_upvotes(data) {
            var margin = { top: 20, right: 20, bottom: 70, left: 50 },
                width = 900 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;


            // set the ranges
            var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.05);
            var y = d3.scale.linear().range([height, 0]);

            // define the axis
            var xAxis = d3.svg.axis()
                .scale(x)
                .orient("bottom");


            var yAxis = d3.svg.axis()
                .scale(y)
                .orient("left")
                .ticks(10);


            // add the SVG element
            var svg = d3.select("#working-bugs-upvotes").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)

                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            x.domain(data.map(function(d) { return d.title; }));
            y.domain([0, d3.max(data, function(d) { return d.total_upvotes; })]);

            // add axis
            svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .style({ 'stroke': 'black', 'fill': 'none', 'stroke-width': '1px' })
                .call(xAxis)
                .selectAll("text")
                .classed('labels', true)
                .style("text-anchor", "middle", { 'fill': 'black' })
                .attr("dx", "-.8em")
                .attr("dy", "-.15em")
                .attr("transform", "translate(0, 20)");


            svg.append("g")
                .attr("class", "y axis")
                .style({ 'stroke': 'black', 'fill': 'none', 'stroke-width': '1px' })
                .call(yAxis)
                .append("text")
                .attr("transform", "rotate(-90), translate(-100, -45)")
                .attr("y", 5)
                .attr("dy", ".71em")
                .classed('labels', true)
                .style("text-anchor", "middle")
                .text("Upvotes");


            // Add bar chart
            svg.selectAll("bar")
                .data(data)
                .enter().append("rect")
                .style('fill', 'rgb(49, 130, 189)')
                .attr("class", "bar")
                .attr("x", function(d) { return x(d.title); })
                .attr("width", x.rangeBand())
                .attr("y", function(d) { return y(d.total_upvotes); })
                .attr("height", function(d) { return height - y(d.total_upvotes); });
        }
    };
    const OpenBugUpvotesApi = function() {
        this.init = function() {
            queue()
                .defer(d3.json, "/stats/api/chart/data/bug/open/upvotes")
                .await(makeGraphs);
        };

        function makeGraphs(error, data) {
            data.forEach(function(d) {
                d.title = d.title;
                d.total_upvotes = +d.total_upvotes;
            });

            console.log(data);
            show_open_working_bug_upvotes(data);
            dc.renderAll();
        }

        function show_open_working_bug_upvotes(data) {
            var margin = { top: 20, right: 20, bottom: 70, left: 50 },
                width = 900 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;


            // set the ranges
            var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.05);
            var y = d3.scale.linear().range([height, 0]);

            // define the axis
            var xAxis = d3.svg.axis()
                .scale(x)
                .orient("bottom");


            var yAxis = d3.svg.axis()
                .scale(y)
                .orient("left")
                .ticks(10);


            // add the SVG element
            var svg = d3.select("#open-bugs-upvotes").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)

                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            x.domain(data.map(function(d) { return d.title; }));
            y.domain([0, d3.max(data, function(d) { return d.total_upvotes; })]);

            // add axis
            svg.append("g")
                .attr("class", "x axis")
                .attr("transform", "translate(0," + height + ")")
                .style({ 'stroke': 'black', 'fill': 'none', 'stroke-width': '1px' })
                .call(xAxis)
                .selectAll("text")
                .classed('labels', true)
                .style("text-anchor", "middle", { 'fill': 'black' })
                .attr("dx", "-.8em")
                .attr("dy", "-.15em")
                .attr("transform", "translate(0, 20)");


            svg.append("g")
                .attr("class", "y axis")
                .style({ 'stroke': 'black', 'fill': 'none', 'stroke-width': '1px' })
                .call(yAxis)
                .append("text")
                .attr("transform", "rotate(-90), translate(-100, -45)")
                .attr("y", 5)
                .attr("dy", ".71em")
                .classed('labels', true)
                .style("text-anchor", "middle")
                .text("Upvotes");


            // Add bar chart
            svg.selectAll("bar")
                .data(data)
                .enter().append("rect")
                .style('fill', 'rgb(49, 130, 189)')
                .attr("class", "bar")
                .attr("x", function(d) { return x(d.title); })
                .attr("width", x.rangeBand())
                .attr("y", function(d) { return y(d.total_upvotes); })
                .attr("height", function(d) { return height - y(d.total_upvotes); });
        }
    };

    const S = new BugUpvotesApi();
    const T = new OpenBugUpvotesApi();
    S.init();
    T.init();