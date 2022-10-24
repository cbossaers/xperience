<?php

    function AddVuelo() {  }
    function UpdateVuelo() {  }
    function DeleteVuelo() {  }

    function GetVueloByOriFecha(string $origen, string $fechaSalida, string $fechaLlegada) { 

        $data = http_build_query(array(
            'origen' => $origen,
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
        
        return json_decode($resp, true);
    }

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
        
        return json_decode($resp, true);
    }

    GetVueloByFechaPrecio(100,"2022-03-01","2022-03-01");
?>