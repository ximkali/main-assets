function AssetTable ({data}) {
    if (!data){
        return <P>Loading...</P>
    }


    return (
        <table>
            <thead>
                <tr>
                    <th>Имя ОС</th>
                    <th>Первоначальная стоимость ОС</th>
                    <th> </th>
                    <th> </th>
                </tr>
            </thead>
            <tbody>
                
            </tbody>
        </table>

    );

}