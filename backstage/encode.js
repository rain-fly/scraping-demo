a5 = function (a, b) {
    c = Object.assign(a, b);
    return c
}
cb = function (t, e) {
    var r, n = 0, o = 0;
    if ("object" != typeof t || !e || e.length <= 0)
        return t;
    for (var i = a5({
        mix_mode: n
    }, t), a = 0, c = e.length; a < c; ++a)
        void 0 !== (r = i[e[a]]) && (n |= 1, o |= 1, i[e[a]] = ch(r));
    return i.mix_mode = n, i.fixed_mix_mode = o, i
}

var cg = function (t) {
    for (var e, r = t.toString(), n = [], o = 0; o < r.length; o++)
        0 <= (e = r.charCodeAt(o)) && e <= 127 ? n.push(e) : 128 <= e && e <= 2047 ? (n.push(192 | 31 & e >> 6),
            n.push(128 | 63 & e)) : (2048 <= e && e <= 55295 || 57344 <= e && e <= 65535) && (n.push(224 | 15 & e >> 12),
            n.push(128 | 63 & e >> 6),
            n.push(128 | 63 & e));
    for (var i = 0; i < n.length; i++)
        n[i] &= 255;
    return n
}
ch = function (t) {
    var e = []
        , r = [];
    if (void 0 === t)
        return "";
    r = cg(t);
    for (var n = 0, o = r.length; n < o; ++n)
        e.push((5 ^ r[n]).toString(16));
    return e.join("")
}

encode = function (email, password) {
    var obj = cb({email: email, password: password}, ['email', 'password'])
    return obj
}

var obj = encode('test@qq.com', '123456')
console.log(obj)

// 在 encode.js 文件末尾添加以下代码
module.exports = encode;