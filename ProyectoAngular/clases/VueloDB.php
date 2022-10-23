<?php

    function AddVuelo() {  }
    function UpdateVuelo() {  }
    function DeleteVuelo() {  }

    function GetVueloByFechaPrecio(string $precio, string $fechaSalida, string $fechaLlegada) { 

        $data = http_build_query(array(
            'precio' => $precio,
            'fechaSalida' => $fechaSalida,
            'fechaLlegada' => $fechaLlegada
        ));

        $ch = curl_init();

        $opts = [
            CURLOPT_URL => '88.17.26.37:5000/vuelo' . '?' . $data,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
        ];

        curl_setopt_array($ch, $opts);

        $resp = curl_exec($ch);

        curl_close($ch);
            
        echo $resp;
    }

    getVueloByFechaPrecio(20,'10/04','22/10');

?>