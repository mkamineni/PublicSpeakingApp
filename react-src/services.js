// Load the SDK and UUID
var AWS = require('aws-sdk');
var uuid = require('uuid');

var albumBucketName = 'inkspire';
var bucketRegion = 'us-east-1';
var IdentityPoolId = 'us-east-1:57915198-9208-4e4c-a945-d8925c284e69';


//update the configurations for AWS to use our credentials
AWS.config.update({
    region: bucketRegion,
    credentials: new AWS.CognitoIdentityCredentials({
        IdentityPoolId: IdentityPoolId
    })
});

//create an S3 instance that we can use to access the databaseph
var s3 = new AWS.S3({
    apiVersion: '2006-03-01',
    params: {
        Bucket: albumBucketName
    }
});

//adds a photo to our S3 database
function addPhoto(file) {
    //get the file out of the upload widget	
    if (!files.length) return;
    var photoKey// = files[0].name;

    data = {
        image_url: photoKey,
    }
    post('/api/profilepicture', data);

    s3.upload({
        Key: photoKey,
        Body: file,
        ACL: 'public-read'
    }, function (err, data) {
        if (err) {
            console.log('There was an error uploading your photo: ', err.message);
        }
        console.log('Successfully uploaded photo.');
    });
}