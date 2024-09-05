import React, { useState } from 'react';
import axios from 'axios';

function AddAsset() {
  const [name, setName] = useState('');
  const [cost, setCost] = useState('');
  const [purchaseDate, setPurchaseDate] = useState('');
  const [usefulLife, setUsefulLife] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('/assets/', {
      name,
      cost: parseFloat(cost),
      purchase_date: purchaseDate,
      useful_life: parseInt(usefulLife, 10),
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <input value={cost} onChange={(e) => setCost(e.target.value)} placeholder="Cost" />
      <input type="date" value={purchaseDate} onChange={(e) => setPurchaseDate(e.target.value)} />
      <input value={usefulLife} onChange={(e) => setUsefulLife(e.target.value)} placeholder="Useful Life (years)" />
      <button type="submit">Add Asset</button>
    </form>
  );
}

export default AddAsset;
