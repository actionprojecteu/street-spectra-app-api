-- CREATE DATABASE streetspectra:
-- CREATE EXTENSION POSTGIS;

CREATE TABLE public.ss_spectra (
	id varchar NOT NULL,
	username varchar(50) NULL, -- Username 
	ts timestamptz NULL, -- UTC observation timestamp
	heading int4 NULL, -- Spectrum heading from North (degrees)
	elevation int4 NULL, -- Picture elevation (degrees)
	description varchar(250) NULL, -- Picture description
	geom geometry NULL,
	CONSTRAINT ss_spectra_pk PRIMARY KEY (id)
);

-- Column comments

COMMENT ON COLUMN public.ss_spectra.username IS 'Username ';
COMMENT ON COLUMN public.ss_spectra.ts IS 'UTC observation timestamp';
COMMENT ON COLUMN public.ss_spectra.heading IS 'Spectrum heading from North (degrees)';
COMMENT ON COLUMN public.ss_spectra.elevation IS 'Picture elevation (degrees)';
COMMENT ON COLUMN public.ss_spectra.description IS 'Picture description';

-- Permissions

ALTER TABLE public.ss_spectra OWNER TO postgres;
GRANT ALL ON TABLE public.ss_spectra TO postgres;
