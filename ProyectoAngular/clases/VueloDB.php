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

    //getVueloByFechaPrecio(20,'10/04','22/10');

    class HTTPRequester {
        /**
         * @description Make HTTP-GET call
         * @param       $url
         * @param       array $params
         * @return      HTTP-Response body or an empty string if the request fails or is empty
         */
        public static function HTTPGet($url, array $params) {
            $query = http_build_query($params); 
            $ch    = curl_init($url.'?'.$query);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HEADER, false);
            $response = curl_exec($ch);
            curl_close($ch);
            return $response;
        }
        /**
         * @description Make HTTP-POST call
         * @param       $url
         * @param       array $params
         * @return      HTTP-Response body or an empty string if the request fails or is empty
         */
        public static function HTTPPost($url, array $params) {
            $query = http_build_query($params);
            $ch    = curl_init();
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_HEADER, false);
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $query);
            $response = curl_exec($ch);
            curl_close($ch);
            return $response;
        }
        /**
         * @description Make HTTP-PUT call
         * @param       $url
         * @param       array $params
         * @return      HTTP-Response body or an empty string if the request fails or is empty
         */
        public static function HTTPPut($url, array $params) {
            $query = \http_build_query($params);
            $ch    = \curl_init();
            \curl_setopt($ch, \CURLOPT_RETURNTRANSFER, true);
            \curl_setopt($ch, \CURLOPT_HEADER, false);
            \curl_setopt($ch, \CURLOPT_URL, $url);
            \curl_setopt($ch, \CURLOPT_CUSTOMREQUEST, 'PUT');
            \curl_setopt($ch, \CURLOPT_POSTFIELDS, $query);
            $response = \curl_exec($ch);
            \curl_close($ch);
            return $response;
        }
        /**
         * @category Make HTTP-DELETE call
         * @param    $url
         * @param    array $params
         * @return   HTTP-Response body or an empty string if the request fails or is empty
         */
        public static function HTTPDelete($url, array $params) {
            $query = \http_build_query($params);
            $ch    = \curl_init();
            \curl_setopt($ch, \CURLOPT_RETURNTRANSFER, true);
            \curl_setopt($ch, \CURLOPT_HEADER, false);
            \curl_setopt($ch, \CURLOPT_URL, $url);
            \curl_setopt($ch, \CURLOPT_CUSTOMREQUEST, 'DELETE');
            \curl_setopt($ch, \CURLOPT_POSTFIELDS, $query);
            $response = \curl_exec($ch);
            \curl_close($ch);
            return $response;
        }
    }


    $url = '88.17.26.37:5000/vuelo';
    $data = array(
        'precio' => $precio,
        'fechaSalida' => $fechaSalida,
        'fechaLlegada' => $fechaLlegada
    );
    echo HTTPRequester::HTTPPost($url, $data);

?>