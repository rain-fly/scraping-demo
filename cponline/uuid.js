// if (typeof localStorage === 'undefined' || localStorage === null) {
//   var LocalStorage = require('node-localstorage').LocalStorage;
//   localStorage = new LocalStorage('./scratch');
// }
uuid = function () {
    for (var e = [], t = "0123456789abcdef", i = 0; i < 36; i++)
        e[i] = t.substr(Math.floor(16 * Math.random()), 1);
    e[14] = "4",
        e[19] = t.substr(3 & e[19] | 8, 1),
        e[8] = e[13] = e[18] = e[23] = "-";
    var a = "slider-" + e.join("")
        , r = "point-" + e.join("");
    // localStorage.getItem("slider") || localStorage.setItem("slider", a),
    // localStorage.getItem("point") || localStorage.setItem("point", r)
    console.log(a)
    return a
}
uuid()