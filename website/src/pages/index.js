import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)} style={{backgroundColor: '#2C4D75', color: '#FFFFFF', padding: '4rem 2rem', textAlign: 'center'}}>
      <div className="container">
        <h1 className="hero__title" style={{fontFamily: 'Segoe UI', fontWeight: 'bold', fontSize: '3rem', letterSpacing: '0.5px'}}>
          {siteConfig.title}
        </h1>
        <p className="hero__subtitle" style={{fontFamily: 'Segoe UI', fontSize: '1.4rem', fontStyle: 'italic', margin: '1rem 0 2rem 0', opacity: '0.9'}}>
          {siteConfig.tagline}
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/matrices"
            style={{backgroundColor: '#FFFFFF', color: '#2C4D75', fontWeight: 'bold', border: 'none', padding: '0.8rem 2rem', borderRadius: '4px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)'}}>
            Access Research Data & Matrices 📊
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Home | ${siteConfig.title}`}
      description="Theological Legal Brief & Historical Reference Matrix">
      <HomepageHeader />
      <main style={{padding: '3rem 0', backgroundColor: '#F8F9FA'}}>
        <div className="container" style={{maxWidth: '900px', margin: '0 auto', fontFamily: 'Segoe UI'}}>
          
          <section style={{backgroundColor: '#FFFFFF', padding: '2.5rem', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.05)', marginBottom: '2rem'}}>
            <h2 style={{color: '#2C4D75', borderBottom: '2px solid #D9D9D9', paddingBottom: '0.5rem', fontWeight: 'bold'}}>
              Project Overview
            </h2>
            <p style={{fontSize: '1.1rem', lineHeight: '1.6', color: '#333333'}}>
              This research brief represents a systematic unraveling of global history, executed by stepping entirely outside of sanitized, humanly manufactured frameworks to allow the Scriptures to define its own terms, its own timelines, and its own people. By integrating <strong>paternal tracking, molecular archaeogenetics, metabolic medicine,</strong> and <strong>scriptural timelines</strong>, this independent study uncovers an unbending ledger of material evidence frozen in the soil.
            </p>
          </section>

          <section style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem'}}>
            <div style={{backgroundColor: '#FFFFFF', padding: '1.8rem', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.05)'}}>
              <h3 style={{color: '#2C4D75', fontWeight: 'bold'}}>🔬 Molecular Genetics</h3>
              <p style={{color: '#555555', lineHeight: '1.5'}}>
                Tracing absolute patrilineal and maternal continuity in the primordial Southern Levant through ancient paleogenomic datasets long before the Bronze or Iron Age horizons.
              </p>
            </div>
            
            <div style={{backgroundColor: '#FFFFFF', padding: '1.8rem', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.05)'}}>
              <h3 style={{color: '#2C4D75', fontWeight: 'bold'}}>🧬 Metabolic Sieve</h3>
              <p style={{color: '#555555', lineHeight: '1.5'}}>
                Analyzing the strict biochemical calibrations of Chromosome 9 (9q22.3) and the ALDOB gene mapping metrics as a pre-engineered metabolic selection filter for the Land of Canaan.
              </p>
            </div>

            <div style={{backgroundColor: '#FFFFFF', padding: '1.8rem', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.05)'}}>
              <h3 style={{color: '#2C4D75', fontWeight: 'bold'}}>🔒 Digital Permanence</h3>
              <p style={{color: '#555555', lineHeight: '1.5'}}>
                Securing academic transparency and un-deplatformable permanence through decentralized mirroring repositories and local cryptographic SHA-256 validation ledgers.
              </p>
            </div>
          </section>

          <div style={{textAlign: 'center', marginTop: '3rem'}}>
            <Link to="/docs/cry_for_israel_unabridged" style={{color: '#2C4D75', fontWeight: 'bold', fontSize: '1.1rem', textDecoration: 'underline'}}>
              Read the Unabridged Master Manuscript →
            </Link>
          </div>

        </div>
      </main>
    </Layout>
  );
}
