import React, { useEffect, useState } from 'react';
import styles from './Dashboard.module.css';
import { fetchPortfolio } from '../../api';

const Dashboard = () => {
  const [portfolio, setPortfolio] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const getPortfolio = async () => {
      try {
        const data = await fetchPortfolio();
        setPortfolio(data);
      } catch (err) {
        setError('Fehler beim Laden des Portfolios');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    getPortfolio();
  }, []);

  return (
    <div className={styles.pageLayout}>
      {/* Container 1: Portfolio Overview */}
      <div className={styles.container}>
        <h1 className={styles.header}>Portfolio Overview</h1>
        <div className={styles.content}>
          {loading && <p>Loading...</p>}
          {error && <p>{error}</p>}
          {!loading && !error && portfolio.length === 0 && <p>Kein Portfolio gefunden</p>}
          {!loading && !error && portfolio.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>Ticker</th>
                  <th>Amount</th>
                  <th>Buy Date</th>
                  <th>Sell Date</th>
                  <th>Buy Price</th>
                  <th>Sell Price</th>
                </tr>
              </thead>
              <tbody>
                {portfolio.map((entry: any) => (
                  <tr key={entry.id}>
                    <td>{entry.ticker}</td>
                    <td>{entry.amount}</td>
                    <td>{entry.buy_date}</td>
                    <td>{entry.sell_date}</td>
                    <td>{entry.buy_price}</td>
                    <td>{entry.sell_price}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>

      {/* Weitere Container */}
      <div className={styles.container}>
        <h2 className={styles.header}>Quantity</h2>
        <div className={styles.content}>
          <p>Table content </p>
        </div>
      </div>

      <div className={styles.container}>
        <h3 className={styles.header}>Allocation</h3>
        <ul className={styles.list}>
          <p>Table content PLACEHOLDER</p>
        </ul>
      </div>

      <div className={styles.container}>
        <h3 className={styles.header}>Sector distribution</h3>
        <p>Table content PLACEHOLDER</p>
      </div>
    </div>
  );
};

export default Dashboard;