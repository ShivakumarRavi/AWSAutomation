accessKeyId = "";
secretKeyId = "";
snapshotId = "";
instanceId = "";
imageId = "";

function authtication() {
    accessKeyId = $('#accessKeyId').val();
    secretKeyId = $('#secretKeyId').val();

    $.ajax({
        url: 'http://127.0.0.1:5000/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ 'accessKeyId': accessKeyId, 'secretKeyId': secretKeyId }),
        error: function() {
            document.getElementById('errorBlock').click();
            $('#errorMessage').html('Error has occured');
            $('#errorHeader').html("Error...");
        },
        success: function(data) {
            document.getElementById('createInstanceBlock').click();
        }
    });
}

function createAMI() {
    snapshotId = $('#shashotId').val();
    instanceId = $('#instanceId').val();
    instanceName = $('#instanceName').val();

    $.ajax({
        url: 'http://127.0.0.1:5000/createami',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
            'accessKeyId': accessKeyId,
            'secretKeyId': secretKeyId,
            'snapshotId': snapshotId,
            'instanceId': instanceId,
            'instanceName': instanceName
        }),
        error: function() {
            document.getElementById('errorBlock').click();
            $('#errorMessage').html('Error has occured');
        },
        success: function(data) {
            if (data["status"] == false) {
                document.getElementById('errorBlock').click();
                $('#errorHeader').html("Error...");
                $('#errorMessage').html(data["error"]);
            } else {
                imageId = data["imageId"];
                runInstance();
            }
        }
    });
}

function runInstance() {
    $.ajax({
        url: 'http://127.0.0.1:5000/runimage',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
            'accessKeyId': accessKeyId,
            'secretKeyId': secretKeyId,
            'imageid': imageId,
        }),
        error: function() {
            document.getElementById('errorBlock').click();
            $('#errorHeader').html("Error...");
            $('#errorMessage').html('Error has occured');
        },
        success: function(data) {
            if (data["status"] == false) {
                document.getElementById('errorBlock').click();
                $('#errorMessage').html(data["error"]);
                $('#errorHeader').html("Error...");
            } else {
                document.getElementById('errorBlock').click();
                $('#errorMessage').html("Instance Running successfuly");
                $('#errorHeader').html("Instance Status");
            }
        }
    });
}