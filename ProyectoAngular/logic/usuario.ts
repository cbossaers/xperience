async function GetUsuarioByCorreo(correo: string) {
    try {
      // 👇️ const response: Response
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      // 👇️ const result: GetUsuarioByCorreoResponse
      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  }
  
  async function AddUsuario(correo: string, nombre: string, apellidos: string, telefono: number, fechaNacimiento: Date) {//puede que sean más o menos parámetros
    try {
      // 👇️ const response: Response
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
          nombre: nombre,
          apellidos: apellidos,
          telefono: telefono,
          fechaNacimiento: fechaNacimiento,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      // 👇️ const result: AddUsuarioResponse
      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  }
  async function UpdateUsuario(correo: string, nombre: string, apellidos: string, telefono: number, fechaNacimiento: Date) { //igual
    try {
      // 👇️ const response: Response
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
          nombre: nombre,
          apellidos: apellidos,
          telefono: telefono,
          fechaNacimiento: fechaNacimiento,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      // 👇️ const result: UpdateUsuarioResponse
      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  }
  async function DeleteUsuario(correo: string) {
    try {
      // 👇️ const response: Response
      const response = await fetch('http://88.17.26.37:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          correo: correo,
        }),
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
      });
  
      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }
  
      // 👇️ const result: DeleteUsuarioResponse
      const result = await response.json()
  
      console.log('result is: ', JSON.stringify(result, null, 4));
  
      return result;
    } catch (error) {
      if (error instanceof Error) {
        console.log('error message: ', error.message);
        return error.message;
      } else {
        console.log('unexpected error: ', error);
        return 'An unexpected error occurred';
      }
    }
  }
