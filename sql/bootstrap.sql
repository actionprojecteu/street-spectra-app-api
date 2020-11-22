-- CREATE DATABASE streetspectra:
-- CREATE EXTENSION POSTGIS;

CREATE TABLE public.ss_spectra (
	id varchar NOT NULL,
	username varchar(50) NULL, -- Username 
	ts timestamptz NULL, -- UtC timestamp onservarion
	heading int4 NULL, -- Heading in degrees of the spectrum from north
	elevation int4 NULL, -- Elevation of the phtotograh in degrees
	description varchar(250) NULL, -- Descriptio of the picture
	geom geometry NULL,
	CONSTRAINT ss_spectra_pk PRIMARY KEY (id)
);

-- Column comments

COMMENT ON COLUMN public.ss_spectra.username IS 'Username ';
COMMENT ON COLUMN public.ss_spectra.ts IS 'UtC timestamp onservarion';
COMMENT ON COLUMN public.ss_spectra.heading IS 'Heading in degrees of the spectrum from north';
COMMENT ON COLUMN public.ss_spectra.elevation IS 'Elevation of the phtotograh in degrees';
COMMENT ON COLUMN public.ss_spectra.description IS 'Descriptio of the picture';

-- Permissions

ALTER TABLE public.ss_spectra OWNER TO postgres;
GRANT ALL ON TABLE public.ss_spectra TO postgres;
