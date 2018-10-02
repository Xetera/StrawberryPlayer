export interface Packet {
    event: string;
    body: any;
    user: string;
}

export interface Song {
    thumbnail?: string;
    title?: string;
    description?: string;
    dateUploaded?: string;
    duration?: number;
    searchedName: string;
}

export const isSong = (obj: any): obj is Song => {
    return 'thumbnail' in obj;
};
