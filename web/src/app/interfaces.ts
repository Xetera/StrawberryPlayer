export interface Packet {
    event: string;
    body: any;
    user: string;
}

export interface IncompleteSong {
    searchedName: string;
}

export interface Song extends IncompleteSong {
    thumbnail: string;
    title: string;
    dateUploaded: string;
    length: number;
}

export const isSong = (obj: any): obj is Song => {
    return 'thumbnail' in obj;
};
