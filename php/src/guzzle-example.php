<?php
 
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client();
$url = 'https://api.cloudways.com/api/v1';

// Below is an example GET request
$response = $client->request('GET', $url, [
    'headers' => [
        'Accept' => 'application/json',
        'Content-type' => 'application/json'
    ]
]);
$body = $response->getBody();

// Alternatively, you can use the syntax below, e.g. for a POST request
$data = array();
$response = $client->post($url, [
    'data' => $data,
    'headers' => [
        'Accept' => 'application/json',
        'Content-type' => 'application/json'
    ]
]);
$body = $response->getBody();