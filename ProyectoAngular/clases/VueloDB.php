<?php

    function AddVuelo() {  }
    function UpdateVuelo() {  }
    function DeleteVuelo() {  }

    function GetVueloByFechaPrecio(string $precio, string $fechaSalida, string $fechaLlegada) { 

        $data = array(
            'precio' => $precio,
            'fechaSalida' => $fechaSalida,
            'fechaLlegada' => $fechaLlegada
        );

        $ch = curl_init();

        $opts = [
            CURLOPT_URL => '88.17.26.37:5000/vuelo',
            CURLOPT_RETURNTRANSFER => true,
            //CURLOPT_CUSTOMREQUEST => 'POST',
            CURLOPT_POST => true,
            //CURLOPT_HTTPHEADER => [ 'Content-Type: application/x-www-form-urlencoded' ],
            CURLOPT_POSTFIELDS => http_build_query($data)
        ];

        curl_setopt_array($ch, $opts);

        $resp = curl_exec($ch);

        curl_close($ch);
            
        echo $resp;
    }

    getVueloByFechaPrecio(20,'10/04','22/10');

?>