type CreateUserResponse = {
  name: string;
  job: string;
  id: string;
  createdAt: string;
};

async function obtenerVuelo() {
  try {
    // 👇️ const response: Response
    const response = await fetch('http://88.17.114.199:5000/vuelo', {
      method: 'POST',
      body: JSON.stringify({
        precio: '100',
        fechaSalida: '2022-03-01',
        fechaLlegada: '2022-03-01',
      }),
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    // 👇️ const result: CreateUserResponse
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

obtenerVuelo();