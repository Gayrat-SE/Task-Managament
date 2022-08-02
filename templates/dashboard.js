<script>
var EchartsPieBasicLights = function() {


//
// Setup module components
//

// Basic pie chart
var _scatterPieBasicLightExamples = function() {
if (typeof echarts == 'undefined') {
    console.warn('Warning - echarts.min.js is not loaded.');
    return;
}

// Define element
var pie_basic_elements = document.getElementById('homeworks');


//
// Charts configuration
//

if (pie_basic_elements) {

    // Initialize chart
    var pie_basic = echarts.init(pie_basic_elements);


    //
    // Chart config
    //

    // Options
    pie_basic.setOption({

        // Colors
        color: [
            '#2ec7c9','#b6a2de','#5ab1ef','#ffb980','#d87a80',
            '#8d98b3','#e5cf0d','#97b552','#95706d','#dc69aa',
            '#07a2a4','#9a7fd1','#588dd5','#f5994e','#c05050',
            '#59678c','#c9ab00','#7eb00a','#6f5553','#c14089'
        ],

        // Global text styles
        textStyle: {
            fontFamily: 'Roboto, Arial, Verdana, sans-serif',
            fontSize: 13
        },

        // Add title
        title: {
            text: 'Информация о Домашних Заданиях',
            left: 'center',
            textStyle: {
                fontSize: 17,
                fontWeight: 500
            },
            subtextStyle: {
                fontSize: 12
            }
        },

        // Add tooltip
        tooltip: {
            trigger: 'item',
            backgroundColor: 'rgba(0,0,0,0.75)',
            padding: [10, 15],
            textStyle: {
                fontSize: 13,
                fontFamily: 'Roboto, sans-serif'
            },
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },

        // Add legend
        legend: {
            orient: 'vertical',
            top: 'center',
            left: 0,
            data: ['Ответы', 'Задание'],
            itemHeight: 8,
            itemWidth: 8
        },

        // Add series
        series: [{
            name: 'Browsers',
            type: 'pie',
            radius: '70%',
            center: ['50%', '57.5%'],
            itemStyle: {
                normal: {
                    borderWidth: 1,
                    borderColor: '#fff'
                }
            },
            data: [
                {value: {{ answer }}, name: 'Ответы'},
                {value: {{ homework }}, name: 'Задание'},
            ]
        }]
    });
}


//
// Resize charts
//

// Resize function
var triggerChartResize = function() {
    pie_basic_elements && pie_basic.resize();
};

// On sidebar width change
var sidebarToggle = document.querySelector('.sidebar-control');
sidebarToggle && sidebarToggle.addEventListener('click', triggerChartResize);

// On window resize
var resizeCharts;
window.addEventListener('resize', function() {
    clearTimeout(resizeCharts);
    resizeCharts = setTimeout(function () {
        triggerChartResize();
    }, 200);
});
};


//
// Return objects assigned to module
//

return {
init: function() {
    _scatterPieBasicLightExamples();
}
}
}();


// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function() {
EchartsPieBasicLights.init();
});

</script>
<script>
var EchartsPieDonutLight = function() {


//
// Setup module components
//

// Basic donut chart
var _scatterPieDonutLightExample = function() {
if (typeof echarts == 'undefined') {
    console.warn('Warning - echarts.min.js is not loaded.');
    return;
}

// Define element
var pie_donut_element = document.getElementById('users');


//
// Charts configuration
//

if (pie_donut_element) {

    // Initialize chart
    var pie_donut = echarts.init(pie_donut_element);


    //
    // Chart config
    //

    // Options
    pie_donut.setOption({

        // Colors
        color: [
            '#2ec7c9','#b6a2de','#5ab1ef','#ffb980','#d87a80',
            '#8d98b3','#e5cf0d','#97b552','#95706d','#dc69aa',
            '#07a2a4','#9a7fd1','#588dd5','#f5994e','#c05050',
            '#59678c','#c9ab00','#7eb00a','#6f5553','#c14089'
        ],

        // Global text styles
        textStyle: {
            fontFamily: 'Roboto, Arial, Verdana, sans-serif',
            fontSize: 13
        },

        // Add title
        title: {
            text: 'Информация о Персонале',
            left: 'center',
            textStyle: {
                fontSize: 17,
                fontWeight: 500
            },
            subtextStyle: {
                fontSize: 12
            }
        },

        // Add tooltip
        tooltip: {
            trigger: 'item',
            backgroundColor: 'rgba(0,0,0,0.75)',
            padding: [10, 15],
            textStyle: {
                fontSize: 13,
                fontFamily: 'Roboto, sans-serif'
            },
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },

        // Add legend
        legend: {
            orient: 'vertical',
            top: 'center',
            left: 0,
            data: ['Ученики', 'Учителя'],
            itemHeight: 8,
            itemWidth: 8
        },

        // Add series
        series: [{
            name: 'Browsers',
            type: 'pie',
            radius: ['50%', '70%'],
            center: ['50%', '57.5%'],
            itemStyle: {
                normal: {
                    borderWidth: 1,
                    borderColor: '#fff'
                }
            },
            data: [
                {value: {{ student_count }}, name: 'Ученики'},
                {value: {{ teacher_count }}, name: 'Учителя'},
            ]
        }]
    });
}


//
// Resize charts
//

// Resize function
var triggerChartResize = function() {
    pie_donut_element && pie_donut.resize();
};

// On sidebar width change
var sidebarToggle = document.querySelector('.sidebar-control');
sidebarToggle && sidebarToggle.addEventListener('click', triggerChartResize);

// On window resize
var resizeCharts;
window.addEventListener('resize', function() {
    clearTimeout(resizeCharts);
    resizeCharts = setTimeout(function () {
        triggerChartResize();
    }, 200);
});
};


//
// Return objects assigned to module
//

return {
init: function() {
    _scatterPieDonutLightExample();
}
}
}();


// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function() {
EchartsPieDonutLight.init();
});

</script>
<script>
    var EchartsPieBasicLight = function() {
    
    
    //
    // Setup module components
    //
    
    // Basic pie chart
    var _scatterPieBasicLightExample = function() {
    if (typeof echarts == 'undefined') {
        console.warn('Warning - echarts.min.js is not loaded.');
        return;
    }
    
    // Define element
    var pie_basic_element = document.getElementById('groups');
    
    
    //
    // Charts configuration
    //
    
    if (pie_basic_element) {
    
        // Initialize chart
        var pie_basic = echarts.init(pie_basic_element);
    
    
        //
        // Chart config
        //
    
        // Options
        pie_basic.setOption({
    
            // Colors
            color: [
                '#2ec7c9','#b6a2de','#5ab1ef','#ffb980','#d87a80',
                '#8d98b3','#e5cf0d','#97b552','#95706d','#dc69aa',
                '#07a2a4','#9a7fd1','#588dd5','#f5994e','#c05050',
                '#59678c','#c9ab00','#7eb00a','#6f5553','#c14089'
            ],
    
            // Global text styles
            textStyle: {
                fontFamily: 'Roboto, Arial, Verdana, sans-serif',
                fontSize: 13
            },
    
            // Add title
            title: {
                text: 'Информация о группах',
                left: 'center',
                textStyle: {
                    fontSize: 17,
                    fontWeight: 500
                },
                subtextStyle: {
                    fontSize: 12
                }
            },
    
            // Add tooltip
            tooltip: {
                trigger: 'item',
                backgroundColor: 'rgba(0,0,0,0.75)',
                padding: [10, 15],
                textStyle: {
                    fontSize: 13,
                    fontFamily: 'Roboto, sans-serif'
                },
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
    
            // Add legend
            legend: {
                orient: 'vertical',
                top: 'center',
                left: 0,
                data: [
                {% for el in groups %}
                '{{ el.name }}',
                {% endfor %}
                ],
                itemHeight: 8,
                itemWidth: 8
            },
    
            // Add series
            series: [{
                name: 'Browsers',
                type: 'pie',
                radius: '70%',
                center: ['50%', '57.5%'],
                itemStyle: {
                    normal: {
                        borderWidth: 1,
                        borderColor: '#fff'
                    }
                },
                data: [
                 {% for el in groups %}
                    {value: {{ el.student.count }}, name: '{{ el.name }}'},
                {% endfor %}
                ]
            }]
        });
    }
    
    
    //
    // Resize charts
    //
    
    // Resize function
    var triggerChartResize = function() {
        pie_basic_element && pie_basic.resize();
    };
    
    // On sidebar width change
    var sidebarToggle = document.querySelector('.sidebar-control');
    sidebarToggle && sidebarToggle.addEventListener('click', triggerChartResize);
    
    // On window resize
    var resizeCharts;
    window.addEventListener('resize', function() {
        clearTimeout(resizeCharts);
        resizeCharts = setTimeout(function () {
            triggerChartResize();
        }, 200);
    });
    };
    
    
    //
    // Return objects assigned to module
    //
    
    return {
    init: function() {
        _scatterPieBasicLightExample();
    }
    }
    }();
    
    
    // Initialize module
    // ------------------------------
    
    document.addEventListener('DOMContentLoaded', function() {
    EchartsPieBasicLight.init();
    });
    
    </script>