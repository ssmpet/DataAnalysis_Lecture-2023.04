from flask import Flask, render_template, request

app = Flask(__name__)
stack = []

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template('08.calc2.html', result=0)
    else:
        try:
            num_ = request.values['num']
        except:
            num_ = None

        try:
            op_ = request.values['op']
        except:
            op_ = None

        if num_ != None:
            stack.append(num_)
            return render_template('08.calc2.html', result=num_)
        if op_ == '=':
            num2 = stack.pop()
            op   = stack.pop()
            num1 = stack.pop()
            result = eval(f'{num1}{op}{num2}')
            return render_template('08.calc2.html', result=result)
        elif op_ == 'C':    # BackSpace 누름
            if len(stack) > 0:
                stack.pop()
            result = stack[-1] if len(stack) > 0 else 0
            
            return  render_template('08.calc2.html', result=result)
        else:               # +, -, *, /, %
            stack.append(op_)
            return render_template('08.calc2.html', result=op_)


if __name__ == '__main__':
    app.run(debug=True)