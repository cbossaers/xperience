<?php 
    ////////////////////////////////////////////////////////////
    //// AÚN FALTA EL ARCHIVO usuario.py PARA QUE FUNCIONEN ////
    ////////////////////////////////////////////////////////////
    function AddUsuario() {  }
    function UpdateUsuario() {  }
    function DeleteUsuario() {  }
    function GetUsuarioByCorreo(string $correo) {
        
        $data = http_build_query(array('correo' => $correo)); #hace falta array?

        $ch = curl_init();

        $opts = [
            CURLOPT_URL => '88.17.26.37:5000/usuario' . '?' . $data,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
        ];

        curl_setopt_array($ch, $opts);

        $resp = curl_exec($ch);

        curl_close($ch);
        
        return json_decode($resp, true);
    }
    function GetUsuarioById(string $id) {

        $data = http_build_query(array('id' => $id,)); #hace falta array?

        $ch = curl_init();

        $opts = [
            CURLOPT_URL => '88.17.26.37:5000/usuario' . '?' . $data,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
        ];

        curl_setopt_array($ch, $opts);

        $resp = curl_exec($ch);

        curl_close($ch);
        
        return json_decode($resp, true);
    }


?>