const BugWorktimeDailyApi = function() {
        this.init = function() {
            queue()
                .defer(d3.json, "/stats/api/chart/data/daily")
                .await(makeGraphs);
        };

        function makeGraphs(error, data) {
            var ndx = crossfilter(data);
            console.log(data);
            show_time_spent_per_bug_pie_chart(ndx);
            dc.renderAll();
        }

        function show_time_spent_per_bug_pie_chart(ndx) {
            var bugDimension = ndx.dimension(function(d) { return d.bug; });
            var bugGroup = bugDimension.group().reduceSum(function(d) { return d.time_spent_mins; });

            dc.pieChart("#bug-worktime")
                .height(220)
                .radius(140)
                .transitionDuration(1500)
                .dimension(bugDimension)
                .group(bugGroup)
                .label(function(d) {
                    if (d.key.length > 12)
                        return d.key.substring(0, 12) + '...';
                    else
                        return d.key;
                });
        }
    };
    const BugWorktimeWeeklyApi = function() {
        this.init = function() {
            queue()
                .defer(d3.json, "/stats/api/chart/data/weekly")
                .await(makeGraphs);
        };

        function makeGraphs(error, data) {
            var ndx = crossfilter(data);
            console.log(data);
            show_time_spent_per_bug_pie_chart_weekly(ndx);
            dc.renderAll();
        }

        function show_time_spent_per_bug_pie_chart_weekly(ndx) {
            var bugDimension = ndx.dimension(function(d) { return d.bug; });
            var bugGroup = bugDimension.group().reduceSum(function(d) { return d.time_spent_mins; });

            dc.pieChart("#bug-worktime-weekly")
                .height(220)
                .radius(140)
                .transitionDuration(1500)
                .dimension(bugDimension)
                .group(bugGroup)
                .label(function(d) {
                    if (d.key.length > 12)
                        return d.key.substring(0, 12) + '...';
                    else
                        return d.key;
                });
        }
    };
    const BugWorktimeMonthlyApi = function() {
        this.init = function() {
            queue()
                .defer(d3.json, "/stats/api/chart/data/monthly")
                .await(makeGraphs);
        };

        function makeGraphs(error, data) {
            var ndx = crossfilter(data);
            console.log(data);
            show_time_spent_per_bug_pie_chart_monthly(ndx);
            dc.renderAll();
        }

        function show_time_spent_per_bug_pie_chart_monthly(ndx) {
            var bugDimension = ndx.dimension(function(d) { return d.bug; });
            var bugGroup = bugDimension.group().reduceSum(function(d) { return d.time_spent_mins; });

            dc.pieChart("#bug-worktime-monthly")
                .height(220)
                .radius(140)
                .transitionDuration(1500)
                .dimension(bugDimension)
                .group(bugGroup)
                .label(function(d) {
                    if (d.key.length > 12)
                        return d.key.substring(0, 12) + '...';
                    else
                        return d.key;
                });
        }
    };


    const P = new BugWorktimeDailyApi();
    const Q = new BugWorktimeWeeklyApi();
    const R = new BugWorktimeMonthlyApi();

    P.init();
    Q.init();
    R.init();