class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const ans = []
        tokens.forEach(i => {
            // console.log({i, ans})
            if ('+-/*'.includes(i)) {
                let a = ans.pop()
                let b = ans.pop()
                if (i === '+') {
                    // console.log(`${a} + ${b}`)
                    ans.push(a + b);
                } else if (i === '-') {
                    // console.log(`${a} - ${b}`)
                    ans.push(b - a);
                } else if (i === '/') {
                    // console.log(`${a} / ${b}`)
                    ans.push(Math.trunc(b / a));
                } else {
                    // console.log(`${a} * ${b}`)
                    ans.push(a * b);
                }
            } else {
                ans.push(Number(i))
            }
        });
        return ans[0]
    }
}
