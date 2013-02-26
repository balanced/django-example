balanced.init(marketplaceUri);

function responseCallbackHandler(response) {
    switch (response.status) {
        case 400:
            // missing or invalid field - check response.error for details
            console.log(response.error);
            break;
        case 404:
            // your marketplace URI is incorrect
            console.log(response.error);
            break;
        case 201:
            // WOO HOO! MONEY!
            // response.data.uri == URI of the bank account resource you
            // should store this bank account URI to later credit it
            console.log(response.data);
            var $form = $("#credit-card-form");
            // the uri is an opaque token referencing the tokenized bank account
            var cardTokenURI = response.data.uri;
            // append the token as a hidden field to submit to the server
            $('<input>').attr({
                type: 'hidden',
                value: cardTokenURI,
                name: 'balancedCreditCardURI'
            }).appendTo($form);
            $form.get()[0].submit();
    }
}

var tokenizeInstrument = function(e) {
    e.preventDefault();

    var $form = $('#credit-card-form');
    var creditCardData = {
        card_number: $form.find('.cc-number').val(),
        expiration_month: $form.find('.cc-em').val(),
        expiration_year: $form.find('.cc-ey').val(),
        security_code: $form.find('cc-csc').val()
    };

    balanced.card.create(creditCardData, responseCallbackHandler);
};

$('#credit-card-form').submit(tokenizeInstrument);
