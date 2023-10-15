function isSubsequence(s, t) {
    let p1 = 0;
    let l1 = s.length;
    for (let i = 0; i < t.length; i++) {
        if (s[p1] === t[i]) {
            p1++;
        }
        if (p1 === l1) {
            return true;
        }
    }
    return false;
}
