const sendPaymentRequestToApi = require("./4-payment");
const Utils = require('./utils');
const expect = require('chai').expect;
var sinon = require("sinon");

describe('sendPaymentRequestToApi', function() {
  it('Use the stub on calculateNumber', () => {
    const stubNb = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spyConsole = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stubNb.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledWithExactly('The total is: 10')).to.be.true;

    stubNb.restore();
    spyConsole.restore();
  })
})
