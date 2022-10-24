<?php 

    function GetHotelById(string $id) {
        
        $data = http_build_query(array('id' => $id)); #hace falta array?

        $ch = curl_init();

        $opts = [
            CURLOPT_URL => '88.17.26.37:5000/hotel' . '?' . $data,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
        ];

        curl_setopt_array($ch, $opts);

        $resp = curl_exec($ch);

        curl_close($ch);
        
        return json_decode($resp, true);
    }

?>