/* eslint-disable */
import Currency from "./3-currency.js";

export default class Pricing {  
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }
    get amount(){
        return this._amount
    }
    set amount(newAmount){
        if (typeof newAmount !== "number"){
            throw new TypeError("must be number")
        }
        this._amount = newAmount
    }
    get currency(){
        return this._currency
    }
    set currency(newCurrency){
        if (typeof newCurrency !== "currency"){
            throw new TypeError("must be Currency")
        }
        this._currency = newCurrency
    }
    displayFullPrice(){
        return `${this._amount} ${this._currency._name} (${this._currency._code})`
    }
    static convertPrice(amount, conversionRate){
        return amount * conversionRate
    }
}