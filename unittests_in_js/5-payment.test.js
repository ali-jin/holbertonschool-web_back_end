const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');

describe("sendPaymentRequestToApi with hooks", function() {
  let spyConsole;

  beforeEach(() => {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyConsole.restore();
  });

  it('it should log the correct output with 100 and 20', function() {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledWith(spyConsole, 'The total is: 120');
  });
  it('it should log the correct output with 10 and 10', function() {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledWith(spyConsole, 'The total is: 20');
  });
});
