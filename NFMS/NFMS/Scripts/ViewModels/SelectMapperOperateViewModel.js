function selectMapperOperateViewModel() {
    var self = this;

    //设置为可监控变量
    self.operator = {
        //timelimit: ko.observable(operator.timelimit),
        //date: ko.observable(operator.date),
        //element: ko.observable(operator.element),
        //level: ko.observable(operator.level),
        //lon_start: ko.observable(operator.lon_start),
        //lon_finish: ko.observable(operator.lon_finish),
        //lat_start: ko.observable(operator.lat_start),
        //lat_finish:ko.observable(operator.lat_finish),
        //area: ko.observable(operator.area)
        timelimit: ko.observable(),
        date: ko.observable(),
        element: ko.observable(),
        level: ko.observable(),
        lon_start: ko.observable(),
        lon_finish: ko.observable(),
        lat_start: ko.observable(),
        lat_finish: ko.observable(),
        area: ko.observable()
    };

    self.handleSubmit=function(obj){
        sendAjaxRequest("POST", null, "/Forecast/TestGetData",ko.toJS(self.operator));
    }

    //异步提交数据至指定url
    function sendAjaxRequest(httpMethod, callback, url, data) {
        $.ajax(url, {
            type: httpMethod,
            success: callback,
            data: data
        });
    }
}