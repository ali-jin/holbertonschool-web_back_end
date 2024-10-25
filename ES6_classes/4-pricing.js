import Currency from "./3-currency";

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Getters and setters
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  displayFullPrice() {
    const { amount, currency } = this;
    return `${amount} ${currency.name} (${currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
