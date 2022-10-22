<?php

    function AddVuelo() {  }
    function UpdateVuelo() {  }
    function DeleteVuelo() {  }
    function GetVueloByFechaPrecio(string $precio, string $fechaSalida, string $fechaLlegada) { 

        $ch = curl_init();

        $url = '88.17.26.37:5000/vuelo';

        $data = array(
            "precio" => "125",
            "fechaSalida" => "13/10",
            "fechaLlegada"=> "18/10"
        );
        
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

        $resp = curl_exec($ch);

        curl_close($ch);
            
        echo $resp;
}

getVueloByFechaPrecio("20","10/04","22/10");