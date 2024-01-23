const Server = require('../testapp');
const request = require('supertest');
var chai = require('chai');
var chaiHttp = require('chai-http');
chai.use(chaiHttp);
var expect = chai.expect

describe('Hello', () => {
    it('hi', () => 
    chai.request(Server)
        .get('/')
        .then(r => {
            console.log("logging body: " + JSON.stringify(r.test));
            expect(r.text).to.be.equal('Hello World my darling');
        })
    )
});