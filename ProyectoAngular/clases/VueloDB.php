<?php

    function AddVuelo() {  }
    function UpdateVuelo() {  }
    function DeleteVuelo() {  }
    function GetVueloByFechaPrecio(string $precio, string $fechaSalida, string $fechaLlegada) { 
 
    $url = '88.17.26.37:5000';

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, 'precio='.$precio.'&fechaSalida='.$fechaSalida.'&fechaLlegada='.$fechaLlegada);

    /*$endpoint = 'http://example.com/endpoint';
    $params = array('foo' => 'bar');
    $url = $endpoint . '?' . http_build_query($params);
    curl_setopt($ch, CURLOPT_URL, $url);*/

    $resp = curl_exec($ch);
    curl_close($ch);
        
    echo $resp;
}

getVueloByFechaPrecio("20","10/04","22/10");