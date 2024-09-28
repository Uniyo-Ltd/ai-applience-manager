import React, { useState } from 'react';
import axios from 'axios';

interface Appliance {
  id: number;
  model: string;
  price: number; // Changed from string to number
  specification: string;
}

function App() {
  const [appliances, setAppliances] = useState<Appliance[]>([]);
  const [selectedAppliance, setSelectedAppliance] = useState<Appliance | null>(null);
  const [showModal, setShowModal] = useState(false);

  React.useEffect(() => {
    axios.get('/api/appliances/')
      .then(response => {
        setAppliances(response.data);
      })
      .catch(error => {
        console.error('Error fetching appliances:', error);
      });
  }, []);

  const handleOrderClick = (appliance: Appliance) => {
    setSelectedAppliance(appliance);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedAppliance(null);
  };

  return (
    <div className="App">
      <h1>Recommended Appliances for Property Blackhorse Mills Flat 101</h1>
      <table>
        <thead>
          <tr>
            <th>Model</th>
            <th>Price</th>
            <th>Specifications</th>
            <th>Order</th>
          </tr>
        </thead>
        <tbody>
          {appliances.map((appliance) => (
            <tr key={appliance.id}>
              <td>{appliance.model}</td>
              <td>${typeof appliance.price === 'number' ? appliance.price.toFixed(2) : 'N/A'}</td>
              <td>{appliance.specification}</td>
              <td><button onClick={() => handleOrderClick(appliance)}>Order</button></td>
            </tr>
          ))}
        </tbody>
      </table>

      {showModal && selectedAppliance && (
        <div className="modal">
          <div className="modal-content">
            <h2>Schedule Delivery of Selected Appliance</h2>
            <p>Model: {selectedAppliance.model}</p>
            <p>Price: ${typeof selectedAppliance.price === 'number' ? selectedAppliance.price.toFixed(2) : 'N/A'}</p>
            <p>Specifications: {selectedAppliance.specification}</p>
            
            {/* Add form fields for delivery scheduling */}
            <input type="date" placeholder="Delivery Date" />
            <select>
              <option value="">Select Time Window</option>
              <option value="morning">Morning (9am-12pm)</option>
              <option value="afternoon">Afternoon (1pm-4pm)</option>
              <option value="evening">Evening (5pm-8pm)</option>
            </select>

            <button onClick={handleCloseModal}>Cancel</button>
            <button onClick={() => {
              alert(`Order confirmed for ${selectedAppliance.model}`);
              handleCloseModal();
            }}>Confirm Order</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;