import imp
import os
import sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import createTransactionController
from contextlib import closing
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

app = Flask(__name__)
CONSTANTS = imp.load_source('modulename', 'constants.py')

@app.route('/confirmacao')
def mostar_resultado(response):
    render_template('confirmacao.html')

@app.route('/extornoconfirmacao')
def mostar_resultadoextorno(response):
    render_template('extornoconfirmacao.html')

@app.route('/pagamento', methods=['GET', 'POST'])
def charge_credit_card():#tirei amount aqui
    if request.method == "POST":
        """
        Charge a credit card
        """
        # Create a merchantAuthenticationType object with authentication details
        # retrieved from the constants file
        merchantAuth = apicontractsv1.merchantAuthenticationType()
        merchantAuth.name = CONSTANTS.apiLoginId
        merchantAuth.transactionKey = CONSTANTS.transactionKey

        # Create the payment data for a credit card
        creditCard = apicontractsv1.creditCardType()
        creditCard.cardNumber = request.form['cardNumber']
        creditCard.expirationDate = request.form['expirationDate']
        creditCard.cardCode = request.form['cardCode']

        # Add the payment data to a paymentType object
        payment = apicontractsv1.paymentType()
        payment.creditCard = creditCard

        # Create order information
        order = apicontractsv1.orderType()
        order.invoiceNumber = request.form['invoiceNumber']
        order.description = request.form['orderDescription']

        # Set the customer's Bill To address
        customerAddress = apicontractsv1.customerAddressType()
        customerAddress.firstName = request.form['firstName']
        customerAddress.lastName = request.form['lastName']
        customerAddress.company = request.form['company']
        customerAddress.address = request.form['address']
        customerAddress.city = request.form['city']
        customerAddress.state = request.form['state']
        customerAddress.zip = request.form['zip']
        customerAddress.country = request.form['country']



        # Set the customer's identifying information
        customerData = apicontractsv1.customerDataType()
        customerData.type = "individual"
        customerData.id = "90"
        customerData.email = "aindaEstaMockado@gmail.com"

        # Add values for transaction settings
        duplicateWindowSetting = apicontractsv1.settingType()
        duplicateWindowSetting.settingName = "duplicateWindow"
        duplicateWindowSetting.settingValue = "600"
        settings = apicontractsv1.ArrayOfSetting()
        settings.setting.append(duplicateWindowSetting)

        # setup individual line items
        line_item_1 = apicontractsv1.lineItemType()
        line_item_1.itemId = request.form['itemId']
        line_item_1.name = request.form['name']
        line_item_1.description = request.form['description']
        line_item_1.quantity = request.form['quantity']
        line_item_1.unitPrice = request.form['unitPrice']
        '''line_item_2 = apicontractsv1.lineItemType()
        line_item_2.itemId = "67890"
        line_item_2.name = "second"
        line_item_2.description = "Here's the second line item"
        line_item_2.quantity = "3"
        line_item_2.unitPrice = "7.95"'''

        # build the array of line items
        line_items = apicontractsv1.ArrayOfLineItem()
        line_items.lineItem.append(line_item_1)
        #line_items.lineItem.append(line_item_2)

        # Create a transactionRequestType object and add the previous objects to it.
        transactionrequest = apicontractsv1.transactionRequestType()
        transactionrequest.transactionType = "authCaptureTransaction"
        total = float(request.form['quantity']) * float(request.form['unitPrice'])
        transactionrequest.amount = total
        transactionrequest.payment = payment
        transactionrequest.order = order
        transactionrequest.billTo = customerAddress
        transactionrequest.customer = customerData
        transactionrequest.transactionSettings = settings
        transactionrequest.lineItems = line_items
        entrega = apicontractsv1.customerAddressType()
        entrega.firstName = request.form['firstName']
        entrega.lastName = request.form['lastName']
        entrega.company = request.form['company']
        entrega.address = request.form['address']
        entrega.city = request.form['city']
        entrega.state = request.form['state']
        entrega.zip = request.form['zip']
        entrega.country = request.form['country']
        transactionrequest.shipTo = entrega

        # Assemble the complete transaction request
        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = merchantAuth
        createtransactionrequest.refId = "MerchantID-0001"
        createtransactionrequest.transactionRequest = transactionrequest
        # Create the controller
        createtransactioncontroller = createTransactionController(
            createtransactionrequest)
        createtransactioncontroller.execute()

        response = createtransactioncontroller.getresponse()

        if response is not None:
            # Check to see if the API request was successfully received and acted upon
            if response.messages.resultCode == "Ok":
                # Since the API request was successful, look for a transaction response
                # and parse it to display the results of authorizing the card
                if hasattr(response.transactionResponse, 'messages') is True:
                    print(
                        'Successfully created transaction with Transaction ID: %s'
                        % response.transactionResponse.transId)
                    print('Transaction Response Code: %s' %
                          response.transactionResponse.responseCode)
                    print('Message Code: %s' %
                          response.transactionResponse.messages.message[0].code)
                    print('Description: %s' % response.transactionResponse.
                          messages.message[0].description)
                    return render_template('confirmacao.html', response=response)
                else:
                    print('Failed Transaction.')
                    if hasattr(response.transactionResponse, 'errors') is True:
                        print('Error Code:  %s' % str(response.transactionResponse.
                                                      errors.error[0].errorCode))
                        print(
                            'Error message: %s' %
                            response.transactionResponse.errors.error[0].errorText)
                    return render_template('confirmacao.html',response=response)
            # Or, print errors if the API request wasn't successful
            else:
                print('Failed Transaction.')
                if hasattr(response, 'transactionResponse') is True and hasattr(
                        response.transactionResponse, 'errors') is True:
                    print('Error Code: %s' % str(
                        response.transactionResponse.errors.error[0].errorCode))
                    print('Error message: %s' %
                          response.transactionResponse.errors.error[0].errorText)
                else:
                    print('Error Code: %s' %
                          response.messages.message[0]['code'].text)
                    print('Error message: %s' %
                          response.messages.message[0]['text'].text)
                return render_template('confirmacao.html', response=response)
        else:
            print('Null Response.')
            return render_template('pagamento.html')

        return render_template('pagamento.html')
    return render_template('pagamento.html')

@app.route('/estorno', methods=['GET', 'POST'])
def refund_credit_card():#tirei amount aqui
    if request.method == "POST":
        merchantAuth = apicontractsv1.merchantAuthenticationType()
        merchantAuth.name = CONSTANTS.apiLoginId
        merchantAuth.transactionKey = CONSTANTS.transactionKey

        creditCard = apicontractsv1.creditCardType()
        creditCard.cardNumber = request.form['CardNumber']
        creditCard.expirationDate = request.form['ExpirationDate']

        payment = apicontractsv1.paymentType()
        payment.creditCard = creditCard

        transactionrequest = apicontractsv1.transactionRequestType()
        transactionrequest.transactionType = "refundTransaction"
        transactionrequest.amount = request.form['Amount']
        #set refTransId to transId of a settled transaction
        transactionrequest.transId = request.form['RefTransId']
        transactionrequest.refTransId = ''#request.form['RefTransId']
        transactionrequest.payment = payment


        createtransactionrequest = apicontractsv1.createTransactionRequest()
        createtransactionrequest.merchantAuthentication = merchantAuth
        createtransactionrequest.refId = "MerchantID-0001"

        createtransactionrequest.transactionRequest = transactionrequest
        createtransactioncontroller = createTransactionController(createtransactionrequest)
        createtransactioncontroller.execute()

        response = createtransactioncontroller.getresponse()

        if response is not None:
            if response.messages.resultCode == "Ok":
                if hasattr(response.transactionResponse, 'messages') == True:
                    print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId)
                    print ('Transaction Response Code: %s' % response.transactionResponse.responseCode)
                    print ('Message Code: %s' % response.transactionResponse.messages.message[0].code)
                    print ('Description: %s' % response.transactionResponse.messages.message[0].description)
                    return render_template('extornoconfirmacao.html',response=response)
                else:
                    print ('Failed Transaction.')
                    if hasattr(response.transactionResponse, 'errors') == True:
                        print ('Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode))
                        print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
                        return render_template('extornoconfirmacao.html',response=response)
            else:
                print ('Failed Transaction.')
                if hasattr(response, 'transactionResponse') == True and hasattr(response.transactionResponse, 'errors') == True:
                    print ('Error Code: %s' % str(response.transactionResponse.errors.error[0].errorCode))
                    print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
                    return render_template('extornoconfirmacao.html',response=response)
                else:
                    print ('Error Code: %s' % response.messages.message[0]['code'].text)
                    print ('Error message: %s' % response.messages.message[0]['text'].text)
                    return render_template('extornoconfirmacao.html',response=response)
        else:
            print ('Null Response.')

        return response
    return render_template('estorno.html')

if __name__ == '__main__':
    app.run()
'''if (os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    charge_credit_card(CONSTANTS.amount)'''