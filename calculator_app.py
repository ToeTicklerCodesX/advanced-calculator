<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pro Calculator</title>
  <style>
    body {
      background: radial-gradient(circle at top, #1e1e1e, #121212);
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Segoe UI', sans-serif;
      color: white;
    }

    .calculator {
      background: #222;
      padding: 25px;
      border-radius: 15px;
      box-shadow: 0 0 20px rgba(0,0,0,0.5);
      width: 340px;
    }

    .display {
      background: #000;
      color: #0f0;
      font-size: 2em;
      text-align: right;
      padding: 15px;
      border-radius: 10px;
      margin-bottom: 20px;
      overflow-x: auto;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }

    button {
      padding: 20px;
      font-size: 1.2em;
      border: none;
      border-radius: 10px;
      background: #333;
      color: white;
      cursor: pointer;
      transition: 0.2s;
    }

    button:hover {
      background: #444;
    }

    .operator {
      background: #ff9500;
      color: white;
    }

    .operator:hover {
      background: #e08900;
    }

    .equals {
      background: #00b894;
    }

    .equals:hover {
      background: #009874;
    }

    .clear {
      background: #ff3b30;
    }

    .clear:hover {
      background: #d32f2f;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <div class="display" id="display">0</div>
    <div class="buttons">
      <button class="clear" onclick="clearDisplay()">C</button>
      <button onclick="appendValue('(')">(</button>
      <button onclick="appendValue(')')">)</button>
      <button class="operator" onclick="appendValue('/')">÷</button>

      <button onclick="appendValue('7')">7</button>
      <button onclick="appendValue('8')">8</button>
      <button onclick="appendValue('9')">9</button>
      <button class="operator" onclick="appendValue('*')">×</button>

      <button onclick="appendValue('4')">4</button>
      <button onclick="appendValue('5')">5</button>
      <button onclick="appendValue('6')">6</button>
      <button class="operator" onclick="appendValue('-')">−</button>

      <button onclick="appendValue('1')">1</button>
      <button onclick="appendValue('2')">2</button>
      <button onclick="appendValue('3')">3</button>
      <button class="operator" onclick="appendValue('+')">+</button>

      <button onclick="appendValue('0')">0</button>
      <button onclick="appendValue('.')">.</button>
      <button class="equals" onclick="calculate()">=</button>
    </div>
  </div>

  <script>
    let display = document.getElementById('display');
    let expression = '';

    function appendValue(value) {
      if (expression === '0') expression = '';
      expression += value;
      display.textContent = expression;
    }

    function clearDisplay() {
      expression = '';
      display.textContent = '0';
    }

    function calculate() {
      try {
        let result = eval(expression.replace(/÷/g, '/').replace(/×/g, '*'));
        display.textContent = result;
        expression = result.toString();
      } catch {
        display.textContent = 'Error';
        expression = '';
      }
    }
  </script>
</body>
</html>
