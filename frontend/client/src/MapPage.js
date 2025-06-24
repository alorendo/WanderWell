import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
<<<<<<< HEAD
import { useNavigate } from 'react-router-dom';
import Header from './components/header'

const MapPage = () => {
  const [geoData, setGeoData] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('http://127.0.0.1:5000/map') // Your Flask backend route
=======
import Header from './components/Header';

const MapPage = () => {
  const [geoData, setGeoData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/map')
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
      .then(res => res.json())
      .then(data => setGeoData(data))
      .catch(err => console.error('Error loading map data:', err));
  }, []);

  const onEachCountry = (feature, layer) => {
<<<<<<< HEAD
    const code = feature.properties.ISO_A2?.toLowerCase(); // or .ADMIN for name
    layer.on({
      click: () => {
        if (code) navigate(`/country/${code}`);
      },
    });
    layer.bindPopup(feature.properties.ADMIN); // country name popup
=======
    const code = feature.properties["ISO3166-1-Alpha-2"]?.toLowerCase() || '';
    const countryName = feature.properties.name || 'Unknown';

    // Avoid showing links for invalid codes like '-99'
    if (!code || code === '-99') {
      layer.bindPopup('<div><em>Unknown country</em></div>');
      layer.setStyle({ cursor: 'default' });
      return;
    }

    const popupContent = `
      <div>
        <strong>
          <a href="/country/${code}" style="color: blue; text-decoration: underline;">
            ${countryName}
          </a>
        </strong>
      </div>
    `;

    layer.bindPopup(popupContent);
    layer.setStyle({ cursor: 'pointer' });
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <Header />
      <h2 style={{ textAlign: 'center', margin: '20px 0' }}>Interactive Map Page</h2>
<<<<<<< HEAD
    <MapContainer center={[20, 0]} zoom={2} style={{ height: '90vh' }}>
      <TileLayer
        url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        attribution='© OpenStreetMap'
      />
      {geoData && <GeoJSON data={geoData} onEachFeature={onEachCountry} />}
    </MapContainer>
=======
      <MapContainer center={[20, 0]} zoom={2} style={{ height: '90vh' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="© OpenStreetMap"
        />
        {geoData && <GeoJSON data={geoData} onEachFeature={onEachCountry} />}
      </MapContainer>
>>>>>>> a573c7e (Add styled country detail page and clickable country map routing)
    </div>
  );
};

export default MapPage;
